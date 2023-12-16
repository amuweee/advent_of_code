import unittest

from day_05_seed_location import (
    find_destination,
    get_seeds_from_data,
    get_set_of_mappings_from_data,
    solve_part1,
    solve_part2,
)

with open("data/05_sample.txt") as f:
    sample_data = f.readlines()


class TestSeedLocation(unittest.TestCase):
    def test_starting_seeds_is_parsed(self):
        actual = get_seeds_from_data(sample_data)
        expected = [79, 14, 55, 13]
        self.assertEqual(actual, expected)

    def test_all_mapping_is_parsed_from_data(self):
        result = get_set_of_mappings_from_data(sample_data)
        # first set
        actual = result[0]
        expected = [[50, 98, 2], [52, 50, 48]]
        self.assertListEqual(actual, expected)
        # second set
        actual = result[1]
        expected = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
        self.assertListEqual(actual, expected)
        # last set
        actual = result[-1]
        expected = [[60, 56, 37], [56, 93, 4]]
        self.assertListEqual(actual, expected)

    def test_seed_destination_is_correct(self):
        maps = get_set_of_mappings_from_data(sample_data)
        actual = find_destination(79, maps[0])
        self.assertEqual(actual, 81)
        actual = find_destination(81, maps[1])
        self.assertEqual(actual, 81)
        actual = find_destination(81, maps[3])
        self.assertEqual(actual, 74)

    def test_part1_answer(self):
        answer = solve_part1(sample_data)
        self.assertEqual(answer, 35)

    def test_part2_answer(self):
        answer = solve_part2(sample_data)
        self.assertEqual(answer, 46)

if __name__ == "__main__":
    unittest.main()
