from dataclasses import dataclass
from functools import reduce
from itertools import product
from operator import mul
from typing import Optional

with open("data/12.txt") as f:
    data = f.readlines()
    data = [d.strip("\n") for d in data]


@dataclass
class OnsenRow:
    num_onsen: int
    onsen_raw_str: str
    onsen_groups: list[str]
    damage_groups: list[int]

    def match_onsen_group_to_damage_groups(self) -> list[tuple[str, list[int]]]:
        self.match_groups: Optional[list[tuple[str, list[int]]]] = []
        # if len(self.onsen_groups) > len(self.damage_groups):
        #     self.match_groups.append((self.onsen_raw_str, self.damage_groups))
        self.match_groups.append((self.onsen_raw_str, self.damage_groups))
        # else:
        #     while len(self.onsen_groups) > 1:
        #         self.match_groups.append(
        #             (self.onsen_groups.pop(), [self.damage_groups.pop()])
        #         )
        #     self.match_groups.append((self.onsen_groups.pop(), self.damage_groups))

        return self.match_groups


def construct_onsen_row(row: str) -> OnsenRow:
    onsens = row.split()[0]
    onsen_groups = [o for o in onsens.split(".") if o != ""]
    damage_groups = [int(i) for i in row.split()[-1].split(",")]

    return OnsenRow(len(onsens), row, onsen_groups, damage_groups)


def validate_pattern(pattern: str, counts: list[int]) -> bool:
    current_count = 0
    for count in counts:
        try:
            # find next group of consecutive # matching to damage group
            start_index = pattern.index("#" * count, current_count)
        # if can't find sequence
        except ValueError:
            return False
        # if there are extra # before or after, then fail
        if start_index > 0 and pattern[start_index - 1] == "#":
            return False
        end_index = start_index + count
        if end_index < len(pattern) and pattern[end_index] == "#":
            return False
        current_count = end_index + 1

    # make sure there are no extra # outside the damage group
    return pattern.count("#") == sum(counts)


def find_match_possibilities(match: tuple[str, list[int]]) -> int:
    pattern = match[0]
    damage_groups = match[1]

    # generate all combination for ? in pattern
    question_marks = [i for i, char in enumerate(pattern) if char == "?"]
    possible_combinations = product([".", "#"], repeat=len(question_marks))

    valid_combinations = 0
    for combination in possible_combinations:
        # create all possible patterns
        temp_pattern = list(pattern)
        for i, char in zip(question_marks, combination):
            temp_pattern[i] = char
        temp_pattern = "".join(temp_pattern)

        # check if valid
        if validate_pattern(temp_pattern, damage_groups):
            print(
                f"{temp_pattern=}, {damage_groups=}, {validate_pattern(temp_pattern, damage_groups)}"
            )
            valid_combinations += 1

    return valid_combinations


def solve_part_1(data: list[str]) -> int:
    all_valids = 0
    for row in data:
        print("-" * 40)
        print(f"{row=}, {all_valids=}")
        onsen_row = construct_onsen_row(row)
        matched_groups = onsen_row.match_onsen_group_to_damage_groups()
        matches = []
        for match in matched_groups:
            matches.append(find_match_possibilities(match))
        print(f"adding {matches} to total")
        all_valids += reduce(mul, matches)

    print(f"Part 1: {all_valids}")
    return all_valids


if __name__ == "__main__":
    solve_part_1(data)
