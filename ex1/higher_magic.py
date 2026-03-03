from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def new_spell(*args: Any, **kwargs: Any) -> tuple:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return new_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiplicateur(*args: Any, **kwargs: Any) -> int | float:
        return base_spell(*args, **kwargs) * multiplier
    return multiplicateur


def conditional_caster(condition: callable, spell: callable) -> callable:
    def verif(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return verif


def spell_sequence(spells: list[callable]) -> callable:
    def cast_all(*args: Any, **kwargs: Any) -> list[Any]:
        results = []
        for s in spells:
            res = s(*args, **kwargs)
            results.append(res)
        return results
    return cast_all


# 1. Sorts de base
def fire(target: str) -> str: return f"🔥 sur {target}"
def fire2(target: str) -> str: return 10
def ice(target: str) -> str: return f"❄️ sur {target}"
# Un sort simple
def lightning(target: str) -> str: return f"⚡ Éclair sur {target}"


def target_is_small(target: str) -> str: return len(target) < 5


selective_lightning = conditional_caster(target_is_small, lightning)
# 2. Test Combiner
print("----------spell_combiner----------")
double_sort = spell_combiner(fire, ice)
print(double_sort("Orc"))
# 3. Test Amplifier
print("\n----------power_amplifier----------")
super_fire = power_amplifier(fire2, 3)
print(super_fire(10))
# 4. Test Séquence
print("\n----------spell_sequence----------")
mon_combo = spell_sequence([fire, ice])
print(mon_combo("Gobelin"))
print("\n----------Conditional Caster ----------")
print(f"Test Orc : {selective_lightning('Orc')}")
print(f"Test Dragon : {selective_lightning('Dragon')}")
