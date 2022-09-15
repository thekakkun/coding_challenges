import unittest

import day_14

test_input = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''


class TestDay14(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            day_14.parse_input(test_input),
            (
                'NNCB',
                {
                    'CH': 'B',
                    'HH': 'N',
                    'CB': 'H',
                    'NH': 'C',
                    'HB': 'C',
                    'HC': 'B',
                    'HN': 'C',
                    'NN': 'C',
                    'BH': 'H',
                    'NC': 'B',
                    'NB': 'B',
                    'BN': 'B',
                    'BB': 'N',
                    'BC': 'B',
                    'CC': 'N',
                    'CN': 'C'
                }
            )
        )

    def test_apply_process(self):
        (test_template, test_rules) = day_14.parse_input(test_input)
        self.assertEqual(
            day_14.apply_process(test_template, test_rules, steps=1),
            'NCNBCHB'
        )
        self.assertEqual(
            day_14.apply_process(test_template, test_rules, steps=2),
            'NBCCNBBBCBHCB'
        )
        self.assertEqual(
            day_14.apply_process(test_template, test_rules, steps=3),
            'NBBBCNCCNBBNBNBBCHBHHBCHB'
        )

    def test_count_elements(self):
        (test_template, test_rules) = day_14.parse_input(test_input)
        test_polymer = day_14.apply_process(test_template, test_rules)

        self.assertEqual(
            day_14.count_elements(test_polymer, test_rules),
            {
                'B': 1749,
                'C': 298,
                'H': 161,
                'N': 865
            }
        )
        self.assertEqual(
            day_14.count_elements(test_template, test_rules, steps=10),
            {
                'B': 1749,
                'C': 298,
                'H': 161,
                'N': 865
            }
        )


if __name__ == '__main__':
    unittest.main()
