from collections import deque
from typing import List, NamedTuple

with open("data/05.txt") as f:
    data = f.readlines()


def get_seeds_from_data(data: List[str]) -> List[int]:
    seeds = [int(num) for num in data[0].split(":")[-1].split() if num.isdigit()]
    return seeds


def get_set_of_mappings_from_data(data: List[str]) -> List[List[List[int]]]:
    # get all the mappings ints
    lines = [line for line in data[3:] if line[0].isdigit() or line[0] == "\n"]

    # append into a list that contains all the mappins
    maps = []
    coords = []
    for line in lines:
        if line != "\n":
            coords.append([int(i) for i in line.split()])
        else:
            maps.append(coords)
            coords = []
    maps.append(coords)

    return maps


class Map(NamedTuple):
    destination: int
    source: int
    ranges: int


def find_destination(seed: int, map: List[List[int]]) -> int:
    maps = [Map(m[0], m[1], m[2]) for m in map]
    for m in maps:
        upper = m.source + m.ranges
        diff = m.source - m.destination
        if m.source <= seed < upper:
            return seed - diff
    return seed


def solve_part1(data: List[str]) -> int:
    # all the starnting seeds
    seeds = get_seeds_from_data(data)
    answer = []

    all_maps = get_set_of_mappings_from_data(data)

    for seed in seeds:
        for map in all_maps:
            seed = find_destination(seed, map)
        answer.append(seed)

    print(f"Part 1: {min(answer)}")
    return min(answer)


def solve_part2(data: List[str]) -> int:
    # all the starting seeds
    seed_coords = deque(get_seeds_from_data(data))
    all_maps = get_set_of_mappings_from_data(data)
    seeds = []
    answer = None
    while len(seed_coords) > 0:
        start = seed_coords.popleft()
        end = seed_coords.popleft()
        seeds = [i for i in range(start, start + end)]
        # just compare with whatever is in answer
        for seed in seeds:
            for map in all_maps:
                seed = find_destination(seed, map)
            if not answer:
                answer = seed
            elif seed < answer:
                answer = seed
            else:
                pass

    print(f"Part 2: {answer}")
    return answer


if __name__ == "__main__":
    solve_part1(data)
    solve_part2(data)
