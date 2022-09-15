import unittest

import day_03

test_report = ['00100', '11110', '10110', '10111', '10101',
               '01111', '00111', '11100', '10000', '11001', '00010', '01010']


class TestDay03(unittest.TestCase):
    def test_get_gamma(self):
        self.assertEqual(day_03.get_gamma(test_report), '10110')

    def test_get_rating(self):
        self.assertEqual(day_03.get_rating(test_report, 'o'), '10111')
        self.assertEqual(day_03.get_rating(test_report, 'co2'), '01010')

    def test_diag_1(self):
        self.assertEqual(day_03.diag_1(test_report), 198)

    def test_diag_2(self):
        self.assertEqual(day_03.diag_2(test_report), 230)


if __name__ == '__main__':
    unittest.main()
