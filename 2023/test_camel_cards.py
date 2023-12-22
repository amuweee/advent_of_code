import unittest

from day_07_camel_cards import CamelDeck, Hand, solve_part_1, solve_part_2

with open("data/07_sample.txt") as f:
    sample_data = f.readlines()


# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483


class TestCamelCards(unittest.TestCase):
    def test_hand_is_correctly_constructed(self):
        first_hand = Hand("32T3K", 765)
        self.assertEqual(first_hand._cards, "32T3K")
        self.assertEqual(first_hand._bid, 765)
        self.assertEqual(first_hand[2], "T")
        self.assertEqual(first_hand[-1], "K")

    def test_hand_type_is_assumed_correctly(self):
        self.assertEqual(Hand("32T3K", 1).hand_type(), "one_pair")
        self.assertEqual(Hand("T55T5", 1).hand_type(), "full_house")
        self.assertEqual(Hand("KK677", 1).hand_type(), "two_pair")
        self.assertEqual(Hand("QQQJA", 1).hand_type(), "three_of_a_kind")
        self.assertEqual(Hand("AAAAA", 1).hand_type(), "five_of_a_kind")
        self.assertEqual(Hand("44448", 1).hand_type(), "four_of_a_kind")
        self.assertEqual(Hand("3A7KT", 1).hand_type(), "high_card")

    def test_camel_deck_is_constructed(self):
        actual = CamelDeck(sample_data)
        self.assertEqual(actual[0]._cards, "32T3K")
        self.assertEqual(actual[0]._bid, 765)
        self.assertEqual(actual[-1]._cards, "QQQJA")
        self.assertEqual(actual[-1]._bid, 483)

    def test_hands_are_sorted_by_type_correctly(self):
        actual = CamelDeck(sample_data)._sort_hands_by_rankings()
        self.assertEqual(actual[0]._cards, "32T3K")
        self.assertEqual(actual[1]._cards, "KTJJT")
        self.assertEqual(actual[2]._cards, "KK677")
        self.assertEqual(actual[3]._cards, "T55J5")
        self.assertEqual(actual[4]._cards, "QQQJA")

    def test_part_1_answer(self):
        actual = solve_part_1(sample_data)
        self.assertEqual(actual, 6440)

    def test_hand_type_is_assumed_correctly_with_joker(self):
        self.assertEqual(Hand("32T3K", 1).hand_type_joker(), "one_pair")
        self.assertEqual(Hand("TJ5T5", 1).hand_type_joker(), "full_house")
        self.assertEqual(Hand("KK677", 1).hand_type_joker(), "two_pair")
        self.assertEqual(Hand("QQQJA", 1).hand_type_joker(), "four_of_a_kind")
        self.assertEqual(Hand("AAAAA", 1).hand_type_joker(), "five_of_a_kind")
        self.assertEqual(Hand("444JJ", 1).hand_type_joker(), "five_of_a_kind")
        self.assertEqual(Hand("3A7KT", 1).hand_type_joker(), "high_card")

    def test_hands_are_sorted_by_type_correctly_joker(self):
        actual = CamelDeck(sample_data)._sort_hands_by_rankings_joker()
        self.assertEqual(actual[0]._cards, "32T3K")
        self.assertEqual(actual[1]._cards, "KK677")
        self.assertEqual(actual[2]._cards, "T55J5")
        self.assertEqual(actual[3]._cards, "QQQJA")
        self.assertEqual(actual[4]._cards, "KTJJT")

    def test_part_2_answer(self):
        actual = solve_part_2(sample_data)
        self.assertEqual(actual, 5905)


if __name__ == "__main__":
    unittest.main()
