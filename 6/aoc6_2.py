from collections import Counter


def read_file_into_line_groups(file_path):
    groups = []
    last_idx = 0
    with open(file_path) as f:
        lines = f.readlines()
    for idx in [i for i, v in enumerate(lines) if v == '\n'] + [len(lines)]:
        groups.append([l.strip() for l in lines[last_idx:idx]])
        last_idx = idx + 1
    return groups


pt1, pt2 = (0, 0)
for group in read_file_into_line_groups('answers.txt'):
    answers = [char for line in group for char in line]
    pt1 += len(set(answers))
    pt2 += len([k for k, v in Counter(answers).items() if v == len(group)])


print('Part 1:', pt1)
print('Part 2:', pt2)


assert pt1 == 6506
assert pt2 == 3243
