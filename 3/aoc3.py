def toboggan(lines, over, down):
    offset = 0
    count = 0
    last_line = 0
    ln_length = len(lines[0].strip())

    for i, line in enumerate(lines):
        if last_line + down != i:
            continue

        offset += over
        if offset >= ln_length:
            offset -= ln_length

        if line[offset] == '#':
            count += 1
        last_line = i

    return count


with open('trees.txt') as f:
    lines = f.readlines()

t1 = toboggan(lines, 1, 1)
t2 = toboggan(lines, 3, 1)
t3 = toboggan(lines, 5, 1)
t4 = toboggan(lines, 7, 1)
t5 = toboggan(lines, 1, 2)

print('Part 1:', t2)
print('Part 2:', t1 * t2 * t3 * t4 * t5)
