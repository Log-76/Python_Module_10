from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells, operation):
    # On crée un dictionnaire de correspondance (mapping) operator
    ops = {"add": operator.add,
           "multiply": operator.mul,
           "max": max,
           "min": min}

    # 1. On récupère la fonction correspondante
    func = ops.get(operation)

    if not func:
        raise ValueError(f"Opération '{operation}' non supportée.")
    # 2. On applique reduce :
    # reduce(fonction, séquence)
    return reduce(func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    Crée des versions spécialisées de la fonction d'enchantement fournie.
    Chaque spécialisation fixe la puissance à 50.
    """
    # On crée le dictionnaire avec les fonctions partielles demandées
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
    """
    Crée et configure un système de dispatching pour les sorts.
    """

    @singledispatch
    def cast_spell(spell):
        """Comportement par défaut pour les types inconnus."""
        return f"Unknown magic essence: {spell}"

    @cast_spell.register(int)
    def _(spell):
        """Gestion des dégâts bruts (Integer)."""
        return f"Casting Damage Spell: {spell} points of destruction!"

    @cast_spell.register(str)
    def _(spell):
        """Gestion des enchantements (String)."""
        return f"Casting Enchantment: {spell} spell applied!"

    @cast_spell.register(list)
    def _(spell):
        """Gestion du multi-cast (List)."""
        return (f"Casting Multi-Cast: Triggering {', '.join(map(str, spell))}"
                "simultaneously!")
    # On retourne la fonction configurée
    return cast_spell


print("--- 🧪 DEBUT DES TESTS DU GRIMOIRE ---")

# 1. Test de spell_reducer (Concentration de puissance)
print("\n[1] Test de spell_reducer :")
powers = [10, 20, 30, 5]
total_power = spell_reducer(powers, "add")
max_power = spell_reducer(powers, "max")
print(f" > Puissance cumulée : {total_power} (Attendu: 65)")
print(f" > Sort le plus puissant : {max_power} (Attendu: 30)")


# 2. Test de partial_enchanter (Spécialisation)
print("\n[2] Test de partial_enchanter :")


def base_spell(power, element, target):
    return f"Enchantement {element} sur {target} (Force: {power})"


enchanters = partial_enchanter(base_spell)
# On teste l'enchantement de feu et de foudre
print(f" > {enchanters['fire_enchant'](target='Épée en bois')}")
print(f" > {enchanters['lightning_enchant'](target='Armure de fer')}")


# 3. Test de memoized_fibonacci (Performance)
print("\n[3] Test de memoized_fibonacci :")
# On calcule un grand nombre pour prouver que le cache fonctionne
# Sans lru_cache, 35 prendrait plusieurs secondes, ici c'est instantané.
result = memoized_fibonacci(35)
print(f" > Fibonacci(35) : {result} (Calcul instantané grâce au cache)")


# 4. Test de spell_dispatcher (Polymorphisme)
print("\n[4] Test de spell_dispatcher :")
cast = spell_dispatcher()

print(f" > Entier : {cast(150)}")
print(f" > Texte  : {cast('Bouclier de Mana')}")
print(f" > Liste  : {cast(['Soin', 'Hâte', 'Force'])}")
print(f" > Inconnu: {cast(3.14)}")

print("\n--- ✅ TOUTS LES TESTS SONT TERMINÉS ---")
