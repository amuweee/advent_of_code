# scratchcards

from typing import Dict, List, NamedTuple

with open("data/04.txt") as f:
    data = f.readlines()


class Card(NamedTuple):
    id: int
    winning_numbers: List[int]
    hand_numbers: List[int]


def parse_card(line: str) -> Card:
    id = line.split(":")[0].split()[-1]
    winning_numbers = line.split(":")[-1].split("|")[0]
    hand_numbers = line.split(":")[-1].split("|")[-1]

    card = Card(
        id=int(id),
        winning_numbers=[int(i) for i in winning_numbers.split() if i.isdigit()],
        hand_numbers=[int(i) for i in hand_numbers.split() if i.isdigit()],
    )

    return card


def find_points_for_card(card: Card) -> int:
    matching_count = set(card.winning_numbers) & set(card.hand_numbers)
    if len(matching_count) == 0:
        return 0
    card_value = 1
    for _ in range(len(matching_count) - 1):
        card_value *= 2

    return card_value


def find_part_1(data: List[str]) -> int:
    total_value = 0
    for line in data:
        card_value = find_points_for_card(parse_card(line))
        total_value += card_value
    print(f"Part 1: {total_value}")
    return total_value


def find_id_of_copies_for_a_card(card: Card) -> List[int]:
    matching_count = len(set(card.winning_numbers) & set(card.hand_numbers))
    return list(range(card.id + 1, card.id + matching_count + 1))


def create_card_index_from_lines(lines: List[str]) -> Dict[int, Card]:
    card_index = {parse_card(line).id: parse_card(line) for line in lines}
    return card_index


def find_part_2(data: List[str]) -> int:
    total_card = 0

    # get all cards parsed
    card_index = create_card_index_from_lines(data)

    # create a dict to track all the card copies
    card_tracker = {card_id: 1 for card_id in card_index.keys()}

    # let the cards make copies
    for card_id in card_index.keys():
        # print(card_tracker)

        # add the counts of card being evaluated
        total_card += card_tracker[card_id]
        copies_id = find_id_of_copies_for_a_card(card_index[card_id])
        valid_ids = [c for c in copies_id if c <= len(card_index)]

        # need to loop for number of cards
        for _ in range(card_tracker[card_id]):
            for copied_card_ids in valid_ids:
                card_tracker[copied_card_ids] += 1

    print(f"Part 2: {total_card}")
    return total_card


if __name__ == "__main__":
    find_part_1(data)
    find_part_2(data)
