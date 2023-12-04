from collections import deque
from typing import List, NamedTuple

with open("data/03.txt") as f:
    data = f.readlines()


class Number(NamedTuple):
    value: str
    length: int
    x: int
    y: int


class Symbol(NamedTuple):
    symbol: str
    x: int
    y: int


def parse_number(lines: List[str]) -> List[Number]:
    numbers_list = []
    for x, line in enumerate(lines):
        numbers = deque([(y, char) for y, char in enumerate(line) if char.isdigit()])
        # [(0, "4"), (1, "6"), ...]
        # print(numbers)
        if len(numbers) == 0:
            pass
        else:
            seq_number = [numbers.popleft()]
            while len(numbers) > 0:
                # append sequential items
                if seq_number[-1][0] + 1 == numbers[0][0]:
                    seq_number.append(numbers.popleft())
                # new number starts so make it into namedtuple and recreate seq_number
                else:
                    numbers_list.append(
                        Number(
                            value="".join([a[1] for a in seq_number]),
                            length=len(seq_number),
                            x=x,
                            y=seq_number[0][0],
                        )
                    )
                    seq_number = [numbers.popleft()]

            numbers_list.append(
                Number(
                    value="".join([a[1] for a in seq_number]),
                    length=len(seq_number),
                    x=x,
                    y=seq_number[0][0],
                )
            )

    return numbers_list


def parse_symbol(lines: List[str]) -> List[Symbol]:
    symbols_list = []
    for x, line in enumerate(lines):
        symbols = deque(
            [
                (y, char)
                for y, char in enumerate(line.strip("\n"))
                if not char.isdigit() and not char.isalpha() and char != "."
            ]
        )  # [(3, "*"), ...]
        if symbols:
            for sym in symbols:
                symbols_list.append(
                    Symbol(
                        symbol=sym[1],
                        x=x,
                        y=sym[0],
                    )
                )

    return symbols_list


def find_adjascent_numbers_to_symbol(
    numbers_list: List[Number],
    symbols_list: List[Symbol],
) -> List[int]:
    # find all symbol adjascent positions
    adj_pos = []
    for symbol in symbols_list:
        # ex if symbol.x = 1 and symbol.y = 3 then
        # dot product of [0, 1, 2] and [2, 3, 4]
        x_range = list(i for i in range(symbol.x - 1, symbol.x + 2))
        y_range = list(i for i in range(symbol.y - 1, symbol.y + 2))
        adj_pos += [(x, y) for x in x_range for y in y_range]

    adjascent_numbers = []
    # check each numbers to see if adjascent
    # if symbol is 3 length starting at pos x = 2 and y = 4
    # then its position is [(2,4), (2,5), (2,6)]
    for number in numbers_list:
        number_pos = list(
            (number.x, y) for y in range(number.y, number.y + number.length)
        )
        common_pos = set(number_pos) & set(adj_pos)
        if common_pos:
            adjascent_numbers.append(int(number.value))

    return adjascent_numbers


def find_two_adjascent_numbers_stars(
    numbers_list: List[Number],
    symbols_list: List[Symbol],
) -> int:
    # find all numbers and positions that are considered adjascent
    number_adj_pos = {}
    for number in numbers_list:
        # if symbol is 3 length starting at pos x = 2 and y = 4
        # then its adjuscent is [(2,4), (2,5), (2,6), ...]
        number_adj_pos[number.value] = [
            (number.x, y) for y in range(number.y, number.y + number.length)
        ]

    # for each of the * symbol find adjascent_positions
    gear_ratios = 0
    for symbol in symbols_list:
        # ex if symbol.x = 1 and symbol.y = 3 then
        # dot product of [0, 1, 2] and [2, 3, 4]
        x_range = list(i for i in range(symbol.x - 1, symbol.x + 2))
        y_range = list(i for i in range(symbol.y - 1, symbol.y + 2))
        star_adj_pos = [(x, y) for x in x_range for y in y_range]
        # check there are exactly two numbers adj
        adjascent_numbers = []
        for value, pos in number_adj_pos.items():
            # check for if there are common pos
            if len(set(star_adj_pos) & set(pos)) > 0:
                adjascent_numbers.append(int(value))
        # print(f"{star_adj_pos=}\n{adjascent_numbers=}\n")
        if len(adjascent_numbers) == 2:
            # print(f"before adding {gear_ratios=}\n{adjascent_numbers[0]*adjascent_numbers[1]=}\n")
            gear_ratios += adjascent_numbers[0] * adjascent_numbers[1]
            # print(f"after adding {gear_ratios=}\n")

    return gear_ratios


def find_part_1():
    numbers = parse_number(data)
    symbols = parse_symbol(data)
    eligibles = find_adjascent_numbers_to_symbol(numbers, symbols)
    print(f"Part 1: {sum(eligibles)}")


def find_part_2():
    numbers = parse_number(data)
    symbols = [symbol for symbol in parse_symbol(data) if symbol.symbol == "*"]
    eligibles = find_two_adjascent_numbers_stars(numbers, symbols)
    print(f"Part 2: {eligibles}")


if __name__ == "__main__":
    find_part_1()
    find_part_2()
