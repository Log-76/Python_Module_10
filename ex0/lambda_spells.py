def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = sorted(artifacts, key=lambda artifact: artifact["power"],
                    reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda spell: "*" + spell["name"] + "*", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    result = {"max_power": max(mages, key=lambda mage: mage["power"]),
              "min_power": min(mages, key=lambda mage: mage["power"]),
              "avg_power": sum(map(lambda mage: mage["power"], mages))
              / len(mages)}
    return result


print(artifact_sorter([{"name": "lol", "power": 2, "type": "degat"},
                       {"name": "lol2", "power": 30, "type": "degat"}]))

print(power_filter([{"name": "lol", "power": 2, "type": "degat"},
                    {"name": "lol2", "power": 30, "type": "degat"}], 5))

print(spell_transformer([{"name": "lol", "power": 2, "type": "degat"},
                         {"name": "lol2", "power": 30, "type": "degat"}]))

print(mage_stats([{"name": "lol", "power": 2, "type": "degat"},
                  {"name": "lol2", "power": 30, "type": "degat"}]))
