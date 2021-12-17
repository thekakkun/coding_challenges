# https://adventofcode.com/2021/day/16

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


def read_packet(packet):
    result = []
    while True:
        (v, t) = packet(3), packet(3)
        if v is None or t is None:
            return result
        (v, t) = int(v, 2), int(t, 2)

        if t == 4:
            literal = get_literal(packet)
            result.append({'v': v, 't': t, 'lit': int(literal, 2)})

        else:
            l = packet(1)

            if l is None:
                return result

            elif l == '0':
                bit_length = packet(15)
                if bit_length is None:
                    return result
                bit_length = int(bit_length, 2)
                sub_packet_str = packet(bit_length)
                result.append(
                    {'v': v,
                     't': t,
                     'sub': read_packet(get_bits(sub_packet_str))
                     })

            elif l == '1':
                sub_count = packet(11)
                if sub_count is None:
                    return result
                sub_count = int(sub_count, 2)
                sub_result = []
                while len(sub_result) < sub_count:
                    sub_result += read_packet(packet)
                result.append({
                    'v': v,
                    't': t,
                    'sub': sub_result
                })


def sum_v(trans):
    total = 0
    for e in trans:
        total += e['v']
        if 'sub' in e:
            total += sum_v(e['sub'])

    return total


with open('input/day_16.txt', 'r') as f:
    packet_str = parse_input(f.read())
    packet = get_bits(packet_str)
    trans = read_packet(packet)
    print(sum_v(trans))
