import time
from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps
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
        @wraps
        def valid(power) -> None:
            if power >= min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"
        return valid
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps
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
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
