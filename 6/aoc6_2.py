from collections import Counter, defaultdict


def read_file_into_line_groups(file_path):
    with open(file_path) as f:
        return [[ln for ln in grp.split('\n') if ln] for grp in f.read().split('\n\n')]


pt1, pt2 = (0, 0)
for group in read_file_into_line_groups('answers.txt'):
    answers = [char for line in group for char in line]
    pt1 += len(set(answers))
    pt2 += len([k for k, v in Counter(answers).items() if v == len(group)])


print('Part 1:', pt1)
print('Part 2:', pt2)


assert pt1 == 6506
assert pt2 == 3243
