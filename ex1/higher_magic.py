from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def new_spell(*args, **kwargs) -> str:
        return spell1(*args, **kwargs) + spell2(*args, **kwargs)

    return new_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiplicateur(*args, **kwargs):
        # On appelle le sort de base et on multiplie son résultat
        return base_spell(*args, **kwargs) * multiplier
    return multiplicateur


def conditional_caster(condition: callable, spell: callable) -> callable:
    def verif(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return verif


def spell_sequence(spells: list[callable]) -> callable:
    # *args et **kwargs permettent de recevoir
    # n'importe quel argument (ex: cible, puissance)
    def cast_all(*args, **kwargs) -> list[Any]:
        results = []
        for s in spells:
            # On exécute le sort 's' avec les arguments reçus
            res = s(*args, **kwargs)
            # On ajoute le résultat du sort à notre liste
            results.append(res)
        # On renvoie la liste finale des résultats
        return results
    # IMPORTANT : On renvoie la fonction elle-même
    # (la recette), pas son exécution !
    return cast_all


# 1. Sorts de base
def fire(target): return f"🔥 sur {target}"
def ice(target): return f"❄️ sur {target}"
# Un sort simple
def lightning(target): return f"⚡ Éclair sur {target}"
# Une condition : ne marche que si le nom de la cible est court ( < 5 lettres)
def target_is_small(target): return len(target) < 5


selective_lightning = conditional_caster(target_is_small, lightning)
# 2. Test Combiner
double_sort = spell_combiner(fire, ice)
print(double_sort("Orc"))
# Affiche: 🔥 sur Orc❄️ sur Orc

# 3. Test Amplifier
super_fire = power_amplifier(fire, 3)
print(super_fire("Troll"))
# Affiche: 🔥 sur Troll🔥 sur Troll🔥 sur Troll

# 4. Test Séquence
mon_combo = spell_sequence([fire, ice])
print(mon_combo("Gobelin"))
# Affiche: ['🔥 sur Gobelin', '❄️ sur Gobelin']

print("\n--- Test 5: Conditional Caster ---")

# Cas 1 : La cible est "Orc" (3 lettres, < 5) -> Succès
print(f"Test Orc : {selective_lightning('Orc')}")
# Affiche: ⚡ Éclair sur Orc

# Cas 2 : La cible est "Dragon" (6 lettres, > 5) -> Échec
print(f"Test Dragon : {selective_lightning('Dragon')}")
# Affiche: Spell fizzled
