from dataclasses import dataclass, field
from functools import total_ordering
from io import TextIOBase
from typing import Self

from utils import stopwatch


@dataclass
@total_ordering
class Hand:
    hand: str
    bid: int = field(compare=False)
    use_joker: bool = False

    @classmethod
    def card_rank(cls, card: str, use_joker: bool = False) -> int:
        CARDS = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

        if use_joker and card == "J":
            return -1
        else:
            return CARDS.index(card)

    @classmethod
    def hand_rank(cls, hand: str) -> int:
        KINDS = ("HK", "1P", "2P", "3K", "FH", "4K", "5K")
        return KINDS.index(hand)

    def card_count(self) -> dict[str, int]:
        result = {}

        for card in self.hand:
            result[card] = result.get(card, 0) + 1

        return result

    def __lt__(self, other: Self) -> bool:
        if self.kind == other.kind:
            for self_card, other_card in zip(self.hand, other.hand):
                if self_card == other_card:
                    continue
                return Hand.card_rank(self_card, self.use_joker) < Hand.card_rank(
                    other_card, other.use_joker
                )
            return False

        else:
            return Hand.hand_rank(self.kind) < Hand.hand_rank(other.kind)

    @property
    def kind(self) -> str:
        card_count = self.card_count()

        if self.use_joker:
            # Don't count the "J"s, just add however many there are to whatever we have most
            count = [0 if k == "J" else v for k, v in card_count.items()]
            count.sort()
            count[-1] += card_count.get("J", 0)
        else:
            count = list(card_count.values())

        if 5 in count:
            return "5K"
        elif 4 in count:
            return "4K"
        elif 3 in count:
            if 2 in count:
                return "FH"
            else:
                return "3K"
        elif 2 in count:
            if count.count(2) == 2:
                return "2P"
            else:
                return "1P"
        else:
            return "HK"


@stopwatch
def parse(input: TextIOBase) -> list[Hand]:
    hands = []

    for line in input:
        hand, bid = line.split()
        hands.append(Hand(hand, int(bid)))

    return hands


@stopwatch
def part_1(hands: list[Hand]) -> int:
    sorted_hands = sorted(hands)
    winnings = [(i + 1) * hand.bid for i, hand in enumerate(sorted_hands)]

    return sum(winnings)


@stopwatch
def part_2(hands: list[Hand]) -> int:
    for hand in hands:
        hand.use_joker = True

    sorted_hands = sorted(hands)
    winnings = [(i + 1) * hand.bid for i, hand in enumerate(sorted_hands)]

    return sum(winnings)


if __name__ == "__main__":
    with open("input/day_07.txt", "r") as f:
        hands = parse(f)
        print(part_1(hands))
        print(part_2(hands))
