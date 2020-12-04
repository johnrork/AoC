'Just a start at an experiment with the multiprocessing module, however golang showed more promise'
import datetime
from collections import namedtuple
from multiprocessing.pool import ThreadPool


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


def validator_two(lines):
    inc = 0
    for line in lines:
        md = get_metadata(line)
        p1 = md.min - 1
        p2 = md.max - 1
        if ((md.password[p1] == md.required_char and md.password[p2] != md.required_char) or
                (md.password[p1] != md.required_char and md.password[p2] == md.required_char)):
            inc += 1
    return inc


lines = [l for l in open('passwords.txt')]

pool = ThreadPool(processes=2)

return_val1 = pool.apply_async(validator_two, (lines[0:500],)).get()
return_val2 = pool.apply_async(validator_two, (lines[500:1000],)).get()

print(return_val1 + return_val2)
