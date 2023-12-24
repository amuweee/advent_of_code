import unittest

from day_09_mirage_maintenance import *

with open("data/09_sample.txt") as f:
    sample_data = f.readlines()

# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45


class TestMirageMaintenance(unittest.TestCase):
    def test_input_string_to_int_list(self):
        actual = convert_input_string_to_int_list(sample_data[0])
        self.assertEqual(actual, [0, 3, 6, 9, 12, 15])

    def test_find_step_differences(self):
        int_list = convert_input_string_to_int_list(sample_data[0])
        actual = find_value_difference(int_list)
        self.assertEqual(actual, [3, 3, 3, 3, 3])

    def test_find_all_list_diffs(self):
        actual = get_list_of_all_value_diffs(sample_data[0])
        self.assertListEqual(
            actual, [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
        )

    def test_next_value_is_correctly_found(self):
        all_value_diffs = get_list_of_all_value_diffs(sample_data[0])
        actual = find_next_value(all_value_diffs)
        self.assertEqual(actual, 18)

    def test_part_1(self):
        actual = solve_part_1(sample_data)
        self.assertEqual(actual, 114)

    def test_left_most_value_is_correct(self):
        all_value_diffs = get_list_of_all_value_diffs(sample_data[2])
        actual = find_leftmost_value(all_value_diffs)
        self.assertEqual(actual, 5)

    def test_part_2(self):
        actual = solve_part_2(sample_data)
        self.assertEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
