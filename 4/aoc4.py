import re
from functools import partial

valid = 0
passports = []
current_passport = {}

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            passports.append(current_passport)
            current_passport = {}
            continue

        parts = line.split(' ')
        for p in parts:
            k, v = p.split(':')
            current_passport[k] = v

for p in passports:
    if all(k in p for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        valid += 1

print("Part 1:", valid)


def num_in_range(min, max, value):
    v = int(value)
    if min <= v <= max:
        return value

def matches_pattern(pattern, value):
    match = re.match(pattern, value)
    if match:
        return (value,) + match.groups()

def occurs_in_list(lst, count, value):
    if len([w for w in lst if w == value]) == count:
        return value

def height(value_height_unit):
    _, height, unit = value_height_unit
    if unit == 'cm':
        return num_in_range(150, 193, height)
    return num_in_range(59, 76, height)


requirements = {
    'byr': [partial(num_in_range, 1920, 2002)],
    'iyr': [partial(num_in_range, 2010, 2020)],
    'eyr': [partial(num_in_range, 2020, 2030)],
    'hgt': [partial(matches_pattern, r'^(\d+)(in|cm)$'), partial(height)],
    'hcl': [partial(matches_pattern, r'^#[a-f0-9]{6}$')],
    'ecl': [partial(occurs_in_list, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 1)],
    'pid': [partial(matches_pattern, r'^\d{9}$')],
}

def check_requirements(item):
    for field, validators in requirements.items():
        value = item.get(field)
        if not value:
            return
        for fn in validators:
            value = fn(value)
            if not value:
                return
    return value

count = 0
for  p in passports:
    if check_requirements(p):
        count += 1

print('Part 2:', count)
assert count == 121
