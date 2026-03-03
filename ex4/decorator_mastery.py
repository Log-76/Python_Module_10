import time
import functools
import random
from typing import Any


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        timor = round(end - start, 3)
        print(f"Spell completed in {timor} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[2] if len(args) > 2 else args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for n in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    def __init__(self, guild_name: str) -> None:
        self.guild_name = guild_name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("--- Bienvenue dans la guilde des mages ---")
    mage_name = "Gandalf le Gris"
    if MageGuild.validate_mage_name(mage_name):
        print(f"Nom du mage '{mage_name}' validé.")
    else:
        print("Nom de mage invalide.")
    my_guild = MageGuild("Ordre des Istari")
    print(f"Guilde créée : {my_guild.guild_name}\n")
    print("--- Test de validation de puissance ---")
    print(my_guild.cast_spell("Étincelle", 5))
    print(my_guild.cast_spell("Boule de Feu", 25))
    print("-" * 40 + "\n")

    @retry_spell(max_attempts=3)
    @spell_timer
    def cast_unstable_portal() -> str:
        print("Tentative d'ouverture du portail...")
        if random.random() < 0.7:
            raise RuntimeError("Le portail s'est effondré !")
        return "Portail ouvert avec succès !"

    print("--- Test du sort instable (Retry + Timer) ---")
    final_result = cast_unstable_portal()
    print(f"Résultat final : {final_result}")


main()
