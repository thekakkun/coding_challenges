import unittest

import day_10


class TestDay10(unittest.TestCase):
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

    def test_remove_legal_pairs(self):
        self.assertEqual(
            day_10.remove_legal_pairs(self.test_input[0]),
            '[({([[{{'
        )
        self.assertEqual(
            day_10.remove_legal_pairs(self.test_input[1]),
            '({[<{('
        )

    def test_first_illegal(self):
        self.assertEqual(
            [day_10.first_illegal(line) for line in self.test_input],
            ['', '', '}', '', ')', ']', '', ')', '>', '']
        )

    def test_get_error_score(self):
        self.assertEqual(
            day_10.get_error_score(self.test_input), 26397)

    def test_get_completion(self):
        self.assertEqual(
            day_10.get_completion(self.test_input[0]),
            '}}]])})]'
        )
        self.assertEqual(
            day_10.get_completion(self.test_input[1]),
            ')}>]})'
        )
        self.assertEqual(
            day_10.get_completion(self.test_input[3]),
            '}}>}>))))'
        )

    def test_get_completion_score(self):
        self.assertEqual(
            day_10.get_completion_score(self.test_input),
            288957
        )


if __name__ == '__main__':
    unittest.main()
