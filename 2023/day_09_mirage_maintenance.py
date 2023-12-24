with open("data/09.txt") as f:
    data = f.readlines()


def convert_input_string_to_int_list(line: str) -> list[int]:
    return [int(i) for i in line.split()]


def find_value_difference(nums: list[int]) -> list[int]:
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i + 1] - nums[i])
    return diffs


def get_list_of_all_value_diffs(line: str) -> list[list[int]]:
    all_value_diffs = []
    int_list = convert_input_string_to_int_list(line)
    while len([i for i in int_list if i != 0]) != 0:
        all_value_diffs.append(int_list)
        int_list = find_value_difference(int_list)
    all_value_diffs.append(int_list)

    return all_value_diffs


def find_next_value(value_diffs: list[list[int]]) -> int:
    next_value = 0
    for diffs in value_diffs:
        next_value += diffs[-1]
    return next_value


def solve_part_1(data: list[str]) -> int:
    value_sums = 0
    for line in data:
        all_value_diffs = get_list_of_all_value_diffs(line)
        value_sums += find_next_value(all_value_diffs)

    print(f"Part 1: {value_sums}")
    return value_sums


def find_leftmost_value(value_diffs: list[list[int]]) -> int:
    next_value = [0]
    left_most_vals = [diff[0] for diff in value_diffs]
    left_most_vals.reverse()
    for val in left_most_vals:
        next_value.append(val - next_value[-1])
    return next_value[-1]


def solve_part_2(data: list[str]) -> int:
    value_sums = 0
    for line in data:
        all_value_diffs = get_list_of_all_value_diffs(line)
        value_sums += find_leftmost_value(all_value_diffs)

    print(f"Part 2: {value_sums}")
    return value_sums


if __name__ == "__main__":
    solve_part_1(data)
    solve_part_2(data)
