# https://adventofcode.com/2021/day/16

from functools import reduce


def parse_input(hex_string):
    hex_string = hex_string.strip()
    final_length = len(hex_string) * 4

    return bin(int(hex_string, 16))[2:].zfill(final_length)


def get_bits(packet_str):
    packet_gen = (c for c in packet_str)

    def _f(arg):
        result = ''
        for _ in range(arg):
            try:
                result += next(packet_gen)
            except StopIteration:
                return None
        return result

    return _f


def get_literal(packet):
    literal_bin = ''

    while True:
        (prefix, value) = packet(1), packet(4)
        literal_bin += value

        if prefix == '0':
            return literal_bin


def read_packet(packet, count=None):
    result = []

    while True:
        if count and len(result) == count:
            return result

        (v, t) = packet(3), packet(3)
        if v is None or t is None:
            return result
        (v, t) = int(v, 2), int(t, 2)

        if t == 4:
            literal = get_literal(packet)
            result.append({'v': v, 't': t, 'value': int(literal, 2)})
        else:
            l = packet(1)
            if l == '0':
                bit_length = packet(15)
                if bit_length is None:
                    return result
                bit_length = int(bit_length, 2)
                sub_packet_str = packet(bit_length)
                result.append(
                    {'v': v, 't': t,
                     'sub': read_packet(get_bits(sub_packet_str))
                     })
            elif l == '1':
                sub_count = int(packet(11), 2)
                result.append({
                    'v': v, 't': t,
                    'sub': read_packet(packet, sub_count)
                })


def sum_v(trans):
    total = 0
    for packet in trans:
        total += packet['v']
        if 'sub' in packet:
            total += sum_v(packet['sub'])

    return total


def get_value(trans):
    value_rules = {
        0: lambda x: sum(x),
        1: lambda x: reduce(lambda y, z: y * z, x, 1),
        2: lambda x: min(x),
        3: lambda x: max(x),
        4: lambda x: x[0],
        5: lambda x: 1 if (x[0] > x[1]) else 0,
        6: lambda x: 1 if (x[0] < x[1]) else 0,
        7: lambda x: 1 if (x[0] == x[1]) else 0
    }

    value = []
    for packet in trans:
        if 'value' in packet:
            value.append(packet['value'])
        else:
            value.append(value_rules[packet['t']](get_value(packet['sub'])))
    return value


if __name__ == '__main__':
    with open('input/day_16.txt', 'r') as f:
        packet_str = parse_input(f.read())
        packet = get_bits(packet_str)
        trans = read_packet(packet)
        print(sum_v(trans))
        print(get_value(trans))
