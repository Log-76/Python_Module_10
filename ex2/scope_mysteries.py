from typing import Any


def mage_counter() -> callable:
    score = 0

    def compteur() -> int:
        nonlocal score
        score += 1
        return score
    return compteur


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    result = ""

    def accumulator(item_name: str) -> str:
        nonlocal result
        result = f"{enchantment_type} {item_name}"
        return result
    return accumulator


def memory_vault() -> dict[str, callable]:
    registre = {}

    def store(key: str, value: Any) -> None:
        nonlocal registre
        registre[key] = value

    def recall(key: str) -> str | Any:
        return registre.get(key, "Memory not found")

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
print(power(30))
print(power(9))
print(power(47))
print("----------enchantment_factory----------")
sword = enchantment_factory("Flaming")
print(sword("sword"))
sword = enchantment_factory("Frozen")
print(sword("sword"))
print("----------memory_vault----------")
vault = memory_vault()
vault["store"]("secret_code", 42)
vault["store"]("user_1", "Alice")
print(vault["recall"]("secret_code"))
print(vault["recall"]("user_2"))
