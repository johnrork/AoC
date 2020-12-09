import read

numbers = read.file_into_line_groups('input.txt', int)[0]

def find_two_numbers_totaling(val, lst):
    for i in lst:
        diff = val - i
        if diff in lst:
            return diff

range = [0, 25]
while range[1]+1 < len(numbers):
    last = numbers[range[1]]
    num_range = numbers[range[0]:range[1]]
    if not find_two_numbers_totaling(last, num_range):
        print("Part 1:", last)
        break
    range[0] += 1
    range[1] += 1

total = 0
range = [0, 1]
target = last
while total != target:
    total = sum(numbers[range[0]:range[1]])
    if total < target:
        range[1] += 1
    if total > target:
        range[0] += 1
        range[1] = range[0] + 1

contig = sorted(numbers[range[0]:range[1]])
print("Part 2:", contig[0] + contig[-1])
