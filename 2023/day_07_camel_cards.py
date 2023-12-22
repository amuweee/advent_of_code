from collections import namedtuple

with open("data/07.txt") as f:
    data = f.readlines()

Card = namedtuple("Card", ["rank", "bid"])


class Hand:
    def __init__(self, cards: str, bid: int) -> None:
        self._cards: str = cards
        self._bid: int = bid

    def __repr__(self) -> str:
        return f"Hand:{self._cards} Bid:{self._bid}"

    def __getitem__(self, position) -> str:
        return self._cards[position]

    def _evaluate_hand_type(self) -> str:
        card_count = {}
        for card in self._cards:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1
        combos = list(card_count.values())
        if 5 in combos:
            return "five_of_a_kind"
        elif 4 in combos:
            return "four_of_a_kind"
        elif 3 in combos and 2 in combos:
            return "full_house"
        elif 3 in combos:
            return "three_of_a_kind"
        elif combos.count(2) == 2:
            return "two_pair"
        elif 2 in combos:
            return "one_pair"
        else:
            return "high_card"

    def hand_type(self) -> str:
        return self._evaluate_hand_type()

    def _evaluate_hand_type_joker(self) -> str:
        card_count = {}
        joker_count = 0
        print(f"{self._cards}")
        if self._cards == "JJJJJ":
            return "five_of_a_kind"
        for card in self._cards:
            if card == "J":
                joker_count += 1
            elif card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1
        combos = sorted(list(card_count.values()), reverse=True)
        combos[0] = combos[0] + joker_count
        if 5 in combos:
            return "five_of_a_kind"
        elif 4 in combos:
            return "four_of_a_kind"
        elif 3 in combos and 2 in combos:
            return "full_house"
        elif 3 in combos:
            return "three_of_a_kind"
        elif combos.count(2) == 2:
            return "two_pair"
        elif 2 in combos:
            return "one_pair"
        else:
            return "high_card"

    def hand_type_joker(self) -> str:
        return self._evaluate_hand_type_joker()

class CamelDeck:
    def __init__(self, hands_strings: list[str]) -> None:
        self._deck = [
            Hand(hand.split()[0], int(hand.split()[1])) for hand in hands_strings
        ]

    def __repr__(self) -> str:
        return f"Deck: {self._deck}"

    def __getitem__(self, position) -> Hand:
        return self._deck[position]

    def _sort_hands_by_rankings(self) -> list[Hand]:
        type_ranking = {
            "high_card": 1,
            "one_pair": 2,
            "two_pair": 3,
            "three_of_a_kind": 4,
            "full_house": 5,
            "four_of_a_kind": 6,
            "five_of_a_kind": 7,
        }
        self.all_hands_with_type_rank = {}
        for hand in self._deck:
            hand_type = hand.hand_type()
            type_rank = type_ranking[hand_type]
            if type_rank in self.all_hands_with_type_rank.keys():
                self.all_hands_with_type_rank[type_rank].append(hand)
            else:
                self.all_hands_with_type_rank[type_rank] = [hand]
        self.all_hands_with_type_rank = dict(
            sorted(self.all_hands_with_type_rank.items())
        )

        ranks_ordered = [str(n) for n in range(2, 10)] + list("TJQKA")
        rank_ranking = {key: value for key, value in zip(ranks_ordered, range(1, 14))}

        def get_rank(hand: Hand) -> list[int]:
            chars = hand._cards
            return [rank_ranking.get(c, 0) for c in chars]

        for type_ranking, hands in self.all_hands_with_type_rank.items():
            ranked_hands = sorted(hands, key=get_rank)
            self.all_hands_with_type_rank[type_ranking] = ranked_hands

        new_deck_order = []
        for key in self.all_hands_with_type_rank:
            new_deck_order.extend(self.all_hands_with_type_rank[key])

        self._deck = new_deck_order

        return self._deck


    def _sort_hands_by_rankings_joker(self) -> list[Hand]:
        type_ranking = {
            "high_card": 1,
            "one_pair": 2,
            "two_pair": 3,
            "three_of_a_kind": 4,
            "full_house": 5,
            "four_of_a_kind": 6,
            "five_of_a_kind": 7,
        }
        self.all_hands_with_type_rank = {}
        for hand in self._deck:
            hand_type = hand.hand_type_joker()
            type_rank = type_ranking[hand_type]
            if type_rank in self.all_hands_with_type_rank.keys():
                self.all_hands_with_type_rank[type_rank].append(hand)
            else:
                self.all_hands_with_type_rank[type_rank] = [hand]
        self.all_hands_with_type_rank = dict(
            sorted(self.all_hands_with_type_rank.items())
        )

        ranks_ordered = ["J"] + [str(n) for n in range(2, 10)] + list("TQKA")
        rank_ranking = {key: value for key, value in zip(ranks_ordered, range(1, 14))}

        def get_rank(hand: Hand) -> list[int]:
            chars = hand._cards
            return [rank_ranking.get(c, 0) for c in chars]

        for type_ranking, hands in self.all_hands_with_type_rank.items():
            ranked_hands = sorted(hands, key=get_rank)
            self.all_hands_with_type_rank[type_ranking] = ranked_hands

        new_deck_order = []
        for key in self.all_hands_with_type_rank:
            new_deck_order.extend(self.all_hands_with_type_rank[key])

        self._deck = new_deck_order

        return self._deck


def solve_part_1(lines: list[str]) -> int:
    deck = CamelDeck(lines)
    deck._sort_hands_by_rankings()

    bid_by_rank = zip([hand._bid for hand in deck._deck], range(1, len(deck._deck) + 1))

    winnings = sum(bid * rank for bid, rank in bid_by_rank)

    print(f"Part1: {winnings}")
    return winnings

def solve_part_2(lines: list[str]) -> int:
    deck = CamelDeck(lines)
    deck._sort_hands_by_rankings_joker()

    bid_by_rank = zip([hand._bid for hand in deck._deck], range(1, len(deck._deck) + 1))

    winnings = sum(bid * rank for bid, rank in bid_by_rank)

    print(f"Part2: {winnings}")
    return winnings


if __name__ == "__main__":
    solve_part_1(data)
    solve_part_2(data)
