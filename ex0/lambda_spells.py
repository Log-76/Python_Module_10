def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda artifact: artifact["power"],
                    reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda spell: "* " + spell + " *", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage["power"], mages))
    result = {"max_power": max(powers),
              "min_power": min(powers),
              "avg_power": round(sum(powers) / len(powers), 2)}
    return result


print("----------artifact_sorter----------")
print(artifact_sorter([{"name": "lol", "power": 2, "type": "degat"},
                       {"name": "lol2", "power": 30, "type": "degat"}]))
print("\n----------power_filter----------")
print(power_filter([{"name": "lol", "power": 2, "type": "degat"},
                    {"name": "lol2", "power": 30, "type": "degat"}], 5))
print("\n----------spell_transformer----------")
print(spell_transformer(["lol", "degat", "lol2", "degat"]))
print("\n----------mage_stats----------")
print(mage_stats([{"name": "lol", "power": 2, "type": "degat"},
                  {"name": "lol2", "power": 5, "type": "degat"}]))
