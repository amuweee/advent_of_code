import unittest

from day_04_scratchcards import (
    Card,
    create_card_index_from_lines,
    find_id_of_copies_for_a_card,
    find_part_1,
    find_part_2,
    find_points_for_card,
    parse_card,
)

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

with open("data/04_sample.txt") as f:
    sample_data = f.readlines()


class ScratchpadTests(unittest.TestCase):
    def test_cards_are_parsed_correctly(self):
        # first card
        actual = parse_card(sample_data[0])
        expected = Card(1, [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
        self.assertEqual(actual, expected)
        # second card
        actual = parse_card(sample_data[1])
        expected = Card(2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19])
        self.assertEqual(actual, expected)

    def test_points_are_calculated_correctly_per_card(self):
        # first card
        actual = find_points_for_card(parse_card(sample_data[0]))
        expected = 8
        self.assertEqual(actual, expected)
        # second card
        actual = find_points_for_card(parse_card(sample_data[1]))
        expected = 2
        self.assertEqual(actual, expected)
        # last card
        actual = find_points_for_card(parse_card(sample_data[-1]))
        expected = 0
        self.assertEqual(actual, expected)

    def test_part_1_answer(self):
        actual = find_part_1(sample_data)
        expected = 13
        self.assertEqual(actual, expected)

    def test_copies_of_card_is_parsed_correctly(self):
        # first card
        actual = find_id_of_copies_for_a_card(parse_card(sample_data[0]))
        expected = [2, 3, 4, 5]
        self.assertListEqual(actual, expected, "first card")
        # second card
        actual = find_id_of_copies_for_a_card(parse_card(sample_data[1]))
        expected = [3, 4]
        self.assertListEqual(actual, expected, "second card")
        # last card
        actual = find_id_of_copies_for_a_card(parse_card(sample_data[-1]))
        expected = []
        self.assertListEqual(actual, expected, "last card")

    def test_card_index_if_created_correctly(self):
        actual = create_card_index_from_lines(sample_data[:2])
        expected = {
            1: Card(1, [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
            2: Card(2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        }
        self.assertDictEqual(actual, expected)

    def test_part_2_answer(self):
        actual = find_part_2(sample_data)
        expected = 30
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
