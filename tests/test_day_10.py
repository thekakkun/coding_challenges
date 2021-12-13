import unittest

import day_10

test_input = (
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
)


class TestDay10(unittest.TestCase):
    def test_remove_legal_pairs(self):
        self.assertEqual(
            day_10.remove_legal_pairs(test_input[0]),
            '[({([[{{'
        )
        self.assertEqual(
            day_10.remove_legal_pairs(test_input[1]),
            '({[<{('
        )

    def test_first_illegal(self):
        self.assertEqual(
            [day_10.first_illegal(line) for line in test_input],
            ['', '', '}', '', ')', ']', '', ')', '>', '']
        )

    def test_get_error_score(self):
        self.assertEqual(
            day_10.get_error_score(test_input), 26397)

    def test_get_completion(self):
        self.assertEqual(
            day_10.get_completion(test_input[0]),
            '}}]])})]'
        )
        self.assertEqual(
            day_10.get_completion(test_input[1]),
            ')}>]})'
        )
        self.assertEqual(
            day_10.get_completion(test_input[3]),
            '}}>}>))))'
        )

    def test_get_completion_score(self):
        self.assertEqual(
            day_10.get_completion_score(test_input),
            288957
        )


if __name__ == '__main__':
    unittest.main()
