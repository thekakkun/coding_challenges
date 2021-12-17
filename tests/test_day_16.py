import unittest

import day_16

test_input_1 = 'D2FE28'
test_input_2 = '38006F45291200'
test_input_3 = 'EE00D40C823060'
test_input_4 = '8A004A801A8002F478'
test_input_5 = '620080001611562C8802118E34'
test_input_6 = 'C0015000016115A2E0802F182340'
test_input_7 = 'A0016C880162017C3686B18A3D4780'


class TestDay16(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            day_16.parse_input(test_input_1),
            '110100101111111000101000'
        )
        self.assertEqual(
            day_16.parse_input(test_input_2),
            '00111000000000000110111101000101001010010001001000000000'
        )
        self.assertEqual(
            day_16.parse_input(test_input_3),
            '11101110000000001101010000001100100000100011000001100000'
        )

    def test_read_packet(self):
        test_packet_str_1 = day_16.parse_input(test_input_1)
        test_packet_1 = day_16.get_bits(test_packet_str_1)
        self.assertEqual(
            day_16.read_packet(test_packet_1),
            [{'v': 6, 't': 4, 'lit': 2021}]
        )

        test_packet_str_2 = day_16.parse_input(test_input_2)
        test_packet_2 = day_16.get_bits(test_packet_str_2)
        self.assertEqual(
            day_16.read_packet(test_packet_2),
            [{
                'v': 1,
                't': 6,
                'sub': [
                    {'v': 6, 't': 4, 'lit': 10},
                    {'v': 2, 't': 4, 'lit': 20}
                ]
            }]
        )

        test_packet_str_3 = day_16.parse_input(test_input_3)
        test_packet_3 = day_16.get_bits(test_packet_str_3)
        self.assertEqual(
            day_16.read_packet(test_packet_3),
            [{
                'v': 7,
                't': 3,
                'sub': [
                    {'v': 2, 't': 4, 'lit': 1},
                    {'v': 4, 't': 4, 'lit': 2},
                    {'v': 1, 't': 4, 'lit': 3}
                ]
            }]
        )

    def test_sum_versions(self):
        test_packet_str_4 = day_16.parse_input(test_input_4)
        test_packet_4 = day_16.get_bits(test_packet_str_4)
        test_trans_4 = day_16.read_packet(test_packet_4)
        self.assertEqual(
            day_16.sum_v(test_trans_4),
            16
        )

        test_packet_str_5 = day_16.parse_input(test_input_5)
        test_packet_5 = day_16.get_bits(test_packet_str_5)
        test_trans_5 = day_16.read_packet(test_packet_5)
        self.assertEqual(
            day_16.sum_v(test_trans_5),
            12
        )

        test_packet_str_6 = day_16.parse_input(test_input_6)
        test_packet_6 = day_16.get_bits(test_packet_str_6)
        test_trans_6 = day_16.read_packet(test_packet_6)
        self.assertEqual(
            day_16.sum_v(test_trans_6),
            23
        )

        test_packet_str_7 = day_16.parse_input(test_input_7)
        test_packet_7 = day_16.get_bits(test_packet_str_7)
        test_trans_7 = day_16.read_packet(test_packet_7)
        self.assertEqual(
            day_16.sum_v(test_trans_7),
            31
        )


if __name__ == '__main__':
    unittest.main()
