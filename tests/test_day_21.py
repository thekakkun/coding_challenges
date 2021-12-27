import unittest

import day_21

test_input = '''Player 1 starting position: 4
Player 2 starting position: 8'''


class TestDay21(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(day_21.parse_input(test_input), (3, 7))

    def test_simulate(self):
        test_start = day_21.parse_input(test_input)
        test_rules = [(day_21.iter_die_deterministic(i), 1000)
                      for i in range(2)]
        (score_1, score_2) = [day_21.simulate(test_start[i], test_rules[i])
                              for i in range(2)]

        winning_roll = max(score_1.keys())
        losing_roll = winning_roll-3
        losing_score = list(score_2[losing_roll].keys())[0]

        self.assertEqual((winning_roll + losing_roll) * losing_score, 739785)

    def test_results(self):
        test_start = day_21.parse_input(test_input)
        test_rules = [(day_21.iter_die_deterministic(i), 1000)
                      for i in range(2)]
        scores = [day_21.simulate(test_start[i], test_rules[i])
                  for i in range(2)]
        self.assertEqual(
            day_21.game_results(scores, test_rules[0]),
            [1, 0]
        )

        test_start = day_21.parse_input(test_input)
        test_rules = (day_21.iter_die_dirac(), 21)
        scores = [day_21.simulate(test_start[i], test_rules)
                  for i in range(2)]
        self.assertEqual(
            day_21.game_results(scores, test_rules),
            [444356092776315, 341960390180808]
        )


if __name__ == '__main__':
    unittest.main()
