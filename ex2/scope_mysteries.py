def mage_counter() -> callable:
    score = 0

    def compteur() -> int:
        nonlocal score
        score += 1
        return score
    return compteur


def spell_accumulator(initial_power: int) -> callable:
    power = 0

    def accumulator() -> int:
        nonlocal power
        power += initial_power
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    result = " sword"

    def accumulator() -> int:
        nonlocal result
        result = enchantment_type + result
        return result
    return accumulator


def memory_vault() -> dict[str, callable]:
    registre = {}

    def store(key: str, value: any):
        nonlocal registre
        registre[key] = value

    def recall(key: str):
        return registre.get(key, "Mémoire introuvable")

    return {"store": store,
            "recall": recall}


print("----------mage_counter----------")
mage = mage_counter()
print("id", mage())
print("id", mage())
print("id", mage())
print("id", mage())
print("----------spell_accumulator----------")
power = spell_accumulator(15)
print(power())
print(power())
print(power())
print("----------enchantment_factory----------")
sword = enchantment_factory("Flaming")
print(sword())
sword = enchantment_factory("Frozen")
print(sword())
print("----------memory_vault----------")
vault = memory_vault()
vault["store"]("secret_code", 42)
vault["store"]("user_1", "Alice")
print(vault["recall"]("secret_code"))
print(vault["recall"]("user_2"))
