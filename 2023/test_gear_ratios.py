import unittest

from day_03_gear_ratios import (
    Number,
    Symbol,
    find_adjascent_numbers_to_symbol,
    find_two_adjascent_numbers_stars,
    parse_number,
    parse_symbol,
)

# sample data
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

with open("data/03_sample.txt") as f:
    sample_data = f.readlines()


class TestGearRatios(unittest.TestCase):
    # numbers are parsed correctly into Numbers namedtuple
    def test_numbers_are_parsed_a(self):
        actual = parse_number(sample_data[:3])
        expected = [
            Number("467", 3, 0, 0),
            Number("114", 3, 0, 5),
            Number("35", 2, 2, 2),
            Number("633", 3, 2, 6),
        ]
        self.assertListEqual(actual, expected)

    # symbols are parsed correctly into Symbol namedtuple
    def test_symbols_are_parsed(self):
        actual = parse_symbol(sample_data[:4])
        expected = [Symbol("*", 1, 3), Symbol("#", 3, 6)]
        self.assertListEqual(actual, expected)

    def test_add_all_adjascent_numbers(self):
        numbers = parse_number(sample_data)
        symbols = parse_symbol(sample_data)
        actual = sum(find_adjascent_numbers_to_symbol(numbers, symbols))
        expected = 4361
        self.assertEqual(actual, expected)

    def test_add_all_gear_ratios(self):
        numbers = parse_number(sample_data)
        symbols = [symbol for symbol in parse_symbol(sample_data) if symbol.symbol == "*"]
        actual = find_two_adjascent_numbers_stars(numbers, symbols)
        expected = 467835
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
