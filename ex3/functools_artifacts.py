from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {"add": operator.add,
           "multiply": operator.mul,
           "max": max,
           "min": min}

    func = ops.get(operation)

    if not func:
        raise ValueError(f"Opération '{operation}' non supportée.")
    return reduce(func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element="Fire"),
        'ice_enchant': partial(base_enchantment, power=50, element="Ice"),
        'lightning_enchant': partial(base_enchantment, power=50,
                                     element="Lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return f"Unknown magic essence: {spell}"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Casting Damage Spell: {spell} points of destruction!"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Casting Enchantment: {spell} spell applied!"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return (f"Casting Multi-Cast: Triggering {', '.join(map(str, spell))}"
                "simultaneously!")
    return cast_spell


print("--- 🧪 DEBUT DES TESTS DU GRIMOIRE ---")

print("\n[1] Test de spell_reducer :")
powers = [10, 20, 30, 5]
total_power = spell_reducer(powers, "add")
max_power = spell_reducer(powers, "max")
print(f" > Puissance cumulée : {total_power} (Attendu: 65)")
print(f" > Sort le plus puissant : {max_power} (Attendu: 30)")
print("\n[2] Test de partial_enchanter :")


def base_spell(power: int, element: str, target: str) -> str:
    return f"Enchantement {element} sur {target} (Force: {power})"


enchanters = partial_enchanter(base_spell)
print(f" > {enchanters['fire_enchant'](target='Épée en bois')}")
print(f" > {enchanters['lightning_enchant'](target='Armure de fer')}")
print("\n[3] Test de memoized_fibonacci :")
result = memoized_fibonacci(35)
print(f" > Fibonacci(35) : {result} (Calcul instantané grâce au cache)")
print("\n[4] Test de spell_dispatcher :")
cast = spell_dispatcher()

print(f" > Entier : {cast(150)}")
print(f" > Texte  : {cast('Bouclier de Mana')}")
print(f" > Liste  : {cast(['Soin', 'Hâte', 'Force'])}")
print(f" > Inconnu: {cast(3.14)}")

print("\n--- ✅ TOUTS LES TESTS SONT TERMINÉS ---")
