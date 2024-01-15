from unittest import TestCase, main

from day_12_hot_springs import *

with open("data/12_sample.txt") as f:
    data_sample = f.readlines()
    data_sample = [d.strip("\n") for d in data_sample]

"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


class TestHotSpring(TestCase):
    def test_onsenrow_is_constructed_correctly(self):
        actual_1 = construct_onsen_row("???.### 1,1,3")
        self.assertEqual(actual_1.num_onsen, 7)
        self.assertListEqual(actual_1.onsen_groups, ["???", "###"])
        self.assertListEqual(actual_1.damage_groups, [1, 1, 3])

        actual_2 = construct_onsen_row("?###???????? 3,2,1")
        self.assertEqual(actual_2.num_onsen, 12)
        self.assertListEqual(actual_2.onsen_groups, ["?###????????"])
        self.assertListEqual(actual_2.damage_groups, [3, 2, 1])

    def test_onsen_groups_are_matched_to_brokens(self):
        actual_1 = construct_onsen_row("???.### 1,1,3")
        actual_2 = construct_onsen_row("?###???????? 3,2,1")
        actual_3 = construct_onsen_row("????.######..#####. 1,6,5")
        for element in actual_1.match_onsen_group_to_damage_groups():
            self.assertIn(element, [("???", [1, 1]), ("###", [3])])
        self.assertListEqual(
            actual_2.match_onsen_group_to_damage_groups(), [("?###????????", [3, 2, 1])]
        )
        for element in actual_3.match_onsen_group_to_damage_groups():
            self.assertIn(element, [("????", [1]), ("######", [6]), ("#####", [5])])

    def test_possibilities_are_derived_correctly(self):
        row_1 = find_match_possibilities(("???", [1, 1]))
        self.assertEqual(row_1, 1)
        row_2 = find_match_possibilities(("??", [1]))
        self.assertEqual(row_2, 2)
        row_3 = find_match_possibilities(("?#?#?#?#?#?#?#?", [1, 3, 1, 6]))
        self.assertEqual(row_3, 1)
        row_4 = find_match_possibilities(("????", [4]))
        self.assertEqual(row_4, 1)
        row_5 = find_match_possibilities(("#####", [5]))
        self.assertEqual(row_5, 1)
        row_6 = find_match_possibilities(("?###????????", [3, 2, 1]))
        self.assertEqual(row_6, 10)

    def test_part_1(self):
        actual = solve_part_1(data_sample)
        self.assertEqual(actual, 21)


if __name__ == "__main__":
    main()
