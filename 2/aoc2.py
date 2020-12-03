from collections import namedtuple


pw_metadata = namedtuple('pw_metadata', ['min', 'max', 'required_char', 'password'])


def get_metadata(line):
    policy, password = line.split(': ')
    numbers, char = policy.split(' ')
    min, max = numbers.split('-')
    return pw_metadata(int(min), int(max), char, password)


def validator_one(line):
    md = get_metadata(line)
    count = len([c for c in md.password if c == md.required_char])
    return md.min <= count <= md.max


def validator_two(line):
    md = get_metadata(line)
    p1 = md.min - 1
    p2 = md.max - 1
    return ((md.password[p1] == md.required_char and md.password[p2] != md.required_char) or
            (md.password[p1] != md.required_char and md.password[p2] == md.required_char))


valid_count_one = 0
valid_count_two = 0

for line in open('passwords.txt'):
    if validator_one(line):
        valid_count_one += 1
    if validator_two(line):
        valid_count_two += 1

print('Part 1:', valid_count_one)
print('Part 2:', valid_count_two)
