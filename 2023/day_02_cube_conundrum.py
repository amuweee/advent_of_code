from functools import reduce
from typing import Dict, Tuple

with open("data/02.txt") as f:
    data = f.readlines()


def parse_all_gems_per_hand_per_game(record: str) -> Tuple[int, Dict[str, list[int]]]:
    # get the game number
    game_num = int(record.split(":")[0].split()[1])

    # set counter to return later
    gem_counter = {"red": [], "green": [], "blue": []}

    # get dict of rgb dice counts
    all_results = record.split(": ")[-1].split("; ")
    for records in all_results:
        for gem_counts in records.split(", "):
            color = gem_counts.split()[-1]
            count = int(gem_counts.split()[0])
            gem_counter[color].append(count)

    return (game_num, gem_counter)


possibles = {"red": 12, "green": 13, "blue": 14}
TOTAL = 0
for game in data:
    result = parse_all_gems_per_hand_per_game(game)
    if (
        max(result[1]["red"]) <= possibles["red"]
        and max(result[1]["blue"]) <= possibles["blue"]
        and max(result[1]["green"]) <= possibles["green"]
    ):
        TOTAL += result[0]

print(TOTAL)


# part deux
POWER = 0
for game in data:
    gems_power = 1
    result = parse_all_gems_per_hand_per_game(game)
    for counts in list(result[1].values()):
        gems_power = gems_power * max(counts)
    POWER += gems_power

print(POWER)
