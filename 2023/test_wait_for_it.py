import unittest

from day_06_wait_for_it import (
    answer_part1,
    answer_part2,
    calculate_score,
    get_holding_time_thresholds,
    parse_input_w_kerning,
    parse_inputs,
)

with open("data/06_sample.txt") as f:
    sample_data = f.readlines()

# Time:      7  15   30
# Distance:  9  40  200


class TestWaitForIt(unittest.TestCase):
    def test_inputs_are_parased_correctly(self):
        actual = parse_inputs(sample_data)
        expected = [(7, 9), (15, 40), (30, 200)]
        self.assertListEqual(actual, expected)

    def test_race_scores_are_calculated(self):
        actual_zero = calculate_score(7, 0)
        actual_one = calculate_score(7, 1)
        actual_two = calculate_score(7, 2)
        actual_three = calculate_score(7, 3)
        actual_four = calculate_score(7, 4)
        actual_five = calculate_score(7, 5)
        actual_six = calculate_score(7, 6)
        actual_seven = calculate_score(7, 7)

        self.assertEqual(actual_zero, 0)
        self.assertEqual(actual_one, 6)
        self.assertEqual(actual_two, 10)
        self.assertEqual(actual_three, 12)
        self.assertEqual(actual_four, 12)
        self.assertEqual(actual_five, 10)
        self.assertEqual(actual_six, 6)
        self.assertEqual(actual_seven, 0)

    def test_part1(self):
        actual = answer_part1(sample_data)
        self.assertEqual(actual, 288)

    def test_parse_w_kerning(self):
        actual = parse_input_w_kerning(sample_data)
        self.assertEqual(actual, [71530, 940200])

    def test_holding_time_threshold(self):
        actual = get_holding_time_thresholds(7, 9)
        self.assertEqual(actual, 4)
        actual = get_holding_time_thresholds(15, 40)
        self.assertEqual(actual, 8)
        actual = get_holding_time_thresholds(30, 200)
        self.assertEqual(actual, 9)

    def test_part2(self):
        actual = answer_part2(sample_data)
        self.assertEqual(actual, 71503)


if __name__ == "__main__":
    unittest.main()
