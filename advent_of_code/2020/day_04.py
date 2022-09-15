import re


def day_04(input, required_fields, validate_fields):
    valid_count = 0
    passports = parse_passports(input)

    for e in passports:
        fields = set(e.keys())

        if fields >= required_fields:
            if validate_fields:
                if all([
                    validate_byr(e['byr']),
                    validate_iyr(e['iyr']),
                    validate_eyr(e['eyr']),
                    validate_hgt(e['hgt']),
                    validate_hcl(e['hcl']),
                    validate_ecl(e['ecl']),
                    validate_pid(e['pid']),
                ]):
                    valid_count += 1
            else:
                valid_count += 1

    return valid_count


def validate_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def validate_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


def validate_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


def validate_hgt(hgt):
    if 'cm' in hgt:
        height = int(hgt.replace('cm', ''))
        height_range = [150, 193]
    elif 'in' in hgt:
        height = int(hgt.replace('in', ''))
        height_range = [59, 76]
    else:
        return False

    if height_range[0] <= height <= height_range[1]:
        return True
    else:
        return False


def validate_hcl(hcl):
    if re.search('#([a-f]|[0-9]){6}', hcl):
        return True


def validate_ecl(ecl):

    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False


def validate_pid(pid):
    if re.search('^[\d]{9}$', pid):
        return True
    else:
        return False


def parse_passports(input):
    passport_list = input.strip().split('\n\n')
    passport_list = [x.replace('\n', ' ') for x in passport_list]

    fields = [[y.split(':')[0] for y in x.split(' ')] for x in passport_list]
    data = [[y.split(':')[1] for y in x.split(' ')] for x in passport_list]

    return [dict(zip(k, v)) for k, v in zip(fields, data)]


test_input = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''

invalid_passports = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

valid_passports = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''


required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

# print(day_04(test_input, required_fields, False))
# print(day_04(invalid_passports, required_fields, True))
# print(day_04(valid_passports, required_fields, True))


with open('input/day_04.txt', 'r') as f:
    input = f.read()

    # print(day_04(input, required_fields, False))
    print(day_04(input, required_fields, True))
