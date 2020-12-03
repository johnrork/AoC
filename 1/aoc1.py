def find_two_numbers_totaling(val, lst):
    for i in lst:
        diff = val - i
        if diff in lst:
            return i * diff


def find_three_numbers_totaling(val, lst):
    for i in lst:
        diff = val - i
        match = find_two_numbers_totaling(diff, nums)
        if match:
            return i * match


with open('expenses.txt') as f:
    nums = [int(i) for i in f]
    print('Part 1:', find_two_numbers_totaling(2020, nums))
    print('Part 2:', find_three_numbers_totaling(2020, nums))
