import day_03
import unittest


class TestDay03(unittest.TestCase):
    test_report = ['00100',
                   '11110',
                   '10110',
                   '10111',
                   '10101',
                   '01111',
                   '00111',
                   '11100',
                   '10000',
                   '11001',
                   '00010',
                   '01010']

    def test_diag_1(self):
        self.assertEqual(day_03.diag_1(self.test_report), 198)

    def test_diag_2(self):
        self.assertEqual(day_03.diag_2(self.test_report), 230)

    def test_get_gamma(self):
        self.assertEqual(day_03.get_gamma(self.test_report), '10110')

    def test_get_rating(self):
        self.assertEqual(day_03.get_rating(self.test_report, 'o'), '10111')
        self.assertEqual(day_03.get_rating(self.test_report, 'co2'), '01010')



if __name__ == '__main__':
    unittest.main()
