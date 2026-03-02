import time
import functools
import random


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        timor = end - start
        print(f"[{func.__name__}] Exécuté en {timor:.4f} secondes")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(self, spell_name, power):
            if power < min_power:
                return f"Power {power} is too low!"
            return func(self, spell_name, power)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def retry1(*args, **kwargs) -> None:
            for n in range(1, max_attempts + 1):
                try:
                    # On essaie d'exécuter la fonction originale
                    return func(*args, **kwargs)
                except Exception:
                    # Si ça échoue et qu'il reste des tentatives
                    if n < max_attempts:
                        print("Spell failed, retrying..."
                              f"(attempt {n}/{max_attempts})")
                    else:
                        # Si c'était la dernière tentative
                        return (f"Spell casting failed after {max_attempts}"
                                " attempts")
        return retry1
    return decorator


class MageGuild:
    def __init__(self, guild_name: str):
        self.guild_name = guild_name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():
    print("--- Bienvenue dans la guilde des mages ---")
    # 1. Test du validateur statique
    mage_name = "Gandalf le Gris"
    if MageGuild.validate_mage_name(mage_name):
        print(f"Nom du mage '{mage_name}' validé.")
    else:
        print("Nom de mage invalide.")
    # 2. Initialisation de la guilde
    my_guild = MageGuild("Ordre des Istari")
    print(f"Guilde créée : {my_guild.guild_name}\n")
    # 3. Test de @power_validator
    print("--- Test de validation de puissance ---")
    # Trop faible
    print(my_guild.cast_spell("Étincelle", 5))
    # Puissance suffisante
    print(my_guild.cast_spell("Boule de Feu", 25))
    print("-" * 40 + "\n")
    # 4. Test de @retry_spell et @spell_timer combinés
    # Créons une fonction qui échoue aléatoirement pour le test

    @retry_spell(max_attempts=3)
    @spell_timer
    def cast_unstable_portal():
        print("Tentative d'ouverture du portail...")
        # Simulation d'un échec 70% du temps
        if random.random() < 0.7:
            raise RuntimeError("Le portail s'est effondré !")
        return "Portail ouvert avec succès !"

    print("--- Test du sort instable (Retry + Timer) ---")
    final_result = cast_unstable_portal()
    print(f"Résultat final : {final_result}")


main()
