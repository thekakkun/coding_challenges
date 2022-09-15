import unittest

import day_15

test_input = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''


class TestDay15(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            day_15.parse_input(test_input),
            (
                (1, 1, 6, 3, 7, 5, 1, 7, 4, 2),
                (1, 3, 8, 1, 3, 7, 3, 6, 7, 2),
                (2, 1, 3, 6, 5, 1, 1, 3, 2, 8),
                (3, 6, 9, 4, 9, 3, 1, 5, 6, 9),
                (7, 4, 6, 3, 4, 1, 7, 1, 1, 1),
                (1, 3, 1, 9, 1, 2, 8, 1, 3, 7),
                (1, 3, 5, 9, 9, 1, 2, 4, 2, 1),
                (3, 1, 2, 5, 4, 2, 1, 6, 3, 9),
                (1, 2, 9, 3, 1, 3, 8, 5, 2, 1),
                (2, 3, 1, 1, 9, 4, 4, 5, 8, 1)
            )
        )

    def test_expand_map(self):
        test_risk_map = day_15.parse_input(test_input)
        test_full_risk_map = day_15.expand_map(test_risk_map)
        self.assertEqual(
            test_full_risk_map[0],
            (
                1, 1, 6, 3, 7, 5, 1, 7, 4, 2,
                2, 2, 7, 4, 8, 6, 2, 8, 5, 3,
                3, 3, 8, 5, 9, 7, 3, 9, 6, 4,
                4, 4, 9, 6, 1, 8, 4, 1, 7, 5,
                5, 5, 1, 7, 2, 9, 5, 2, 8, 6
            )
        )
        self.assertEqual(
            test_full_risk_map[-1],
            (
                6, 7, 5, 5, 4, 8, 8, 9, 3, 5,
                7, 8, 6, 6, 5, 9, 9, 1, 4, 6,
                8, 9, 7, 7, 6, 1, 1, 2, 5, 7,
                9, 1, 8, 8, 7, 2, 2, 3, 6, 8,
                1, 2, 9, 9, 8, 3, 3, 4, 7, 9
            )
        )

    def test_get_risk_dijkstra(self):
        test_risk_map = day_15.parse_input(test_input)
        test_dist = day_15.dijkstra(test_risk_map)
        self.assertEqual(test_dist[(9, 9)], 40)

        test_full_risk_map = day_15.expand_map(test_risk_map)
        test_full_dist = day_15.dijkstra(test_full_risk_map)
        self.assertEqual(test_full_dist[(49, 49)], 315)

    def test_get_risk_a_star(self):
        test_risk_map = day_15.parse_input(test_input)
        test_dist = day_15.a_star(test_risk_map, day_15.manhattan)
        self.assertEqual(test_dist[(9, 9)], 40)

        test_full_risk_map = day_15.expand_map(test_risk_map)
        test_full_dist = day_15.a_star(
            test_full_risk_map, day_15.manhattan)
        self.assertEqual(test_full_dist[(49, 49)], 315)


if __name__ == '__main__':
    unittest.main()
