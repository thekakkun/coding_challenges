import time
import os

start_time = time.time()


def p054(hand_list):
    """Poker hands

    Problem 54

    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

        High Card: Highest value card.
        One Pair: Two cards of the same value.
        Two Pairs: Two different pairs.
        Three of a Kind: Three cards of the same value.
        Straight: All cards are consecutive values.
        Flush: All cards of the same suit.
        Full House: Three of a kind and a pair.
        Four of a Kind: Four cards of the same value.
        Straight Flush: All cards are consecutive values of same suit.
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

    If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

    Consider the following five hands dealt to two players:
    Hand    Player 1            Player 2                Winner
    1       5H 5C 6S 7S KD      2C 3S 8S 8D TD          Player 2
            Pair of Fives       Pair of Eights
    2       5D 8C 9S JS AC      2C 5C 7D 8S QH          Player 1
            Highest card Ace    Highest card Queen
    3       2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
            Three Aces          Flush with Diamonds
    4       4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
            Pair of Queens      Pair of Queens
            Highest card Nine   Highest card Seven
    5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
            Full House          Full House
            With Three Fours    with Three Threes

    The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?
    """

    player_1_wins = 0

    for hand in hand_list:
        hand_formatted = [[x[0], x[1]] for x in hand.split(' ')]

        hand_1, hand_2 = hand_formatted[:5], hand_formatted[5:]
        hand_1_score, hand_2_score = poker_score(hand_1), poker_score(hand_2)

        if hand_1_score > hand_2_score:
            player_1_wins += 1

    return player_1_wins


def poker_score(hand):
    card_list = ['2', '3', '4', '5', '6', '7',
                 '8', '9', 'T', 'J', 'Q', 'K', 'A']

    hand_cards = sorted([x[0] for x in hand], key=card_list.index)
    hand_suits = [x[1] for x in hand]

    is_straight, is_flush = False, False

    # Flush check
    if hand_suits.count(hand_suits[0]) == 5:
        is_flush = True

    # Straight check
    straight_start = card_list.index(hand_cards[0])
    for i in range(1, 5):
        if card_list.index(hand_cards[i]) != i + straight_start:
            break
    else:
        is_straight = True

    if is_flush:
        if is_straight:
            if hand_cards == ['T', 'J', 'Q', 'K', 'A']:
                # Royal Flush
                return (10, 12)
            else:
                # Straight Flush
                return (9, card_list.index(hand_cards[4]))
        else:
            # Flush
            return (6, card_list.index(hand_cards[4]))
    elif is_straight:
        # Straight
        return (5, card_list.index(hand_cards[4]))
    else:
        card_count = [hand_cards.count(x) for x in card_list]

        if 4 in card_count:
            # Four of a Kind
            return (8, card_count.index(4), card_count.index(1))
        elif 3 in card_count:
            if 2 in card_count:
                # Full House
                return (7, card_count.index(3), card_count.index(2))
            else:
                # Three of a Kind
                return (4, card_count.index(3),
                        [i for i, x in enumerate(card_count) if x == 1][1],
                        [i for i, x in enumerate(card_count) if x == 1][0]
                        )
        elif 2 in card_count:
            if card_count.count(2) == 2:
                # Two Pair
                return (3, max([i for i, x in enumerate(card_count) if x == 2]),
                        min([i for i, x in enumerate(card_count) if x == 2]), card_count.index(1))
            else:
                # One Pair
                return (2, card_count.index(2)) + tuple(
                    [i for i, x in enumerate(card_count) if x == 1][::-1]
                )
        else:
            # High Card
            return (1,) + tuple(
                [i for i, x in enumerate(card_count) if x == 1][::-1]
            )


with open(os.path.join('level_3', 'p054_poker.txt'), 'r') as f:
    print(p054(f.readlines()))
print('Completed in', time.time() - start_time, 'seconds')
