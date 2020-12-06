max_id = 0
seats = []
my_seat = None


for line in open('seats.txt'):
    rows = range(128)
    cols = range(8)
    for i, char in enumerate(line):
        row_mid = int(len(rows) / 2)
        col_mid = int(len(cols) / 2)

        if char == 'F':
            rows = rows[:row_mid]
        if char == 'B':
            rows = rows[row_mid:]
        if char == 'L':
            cols = cols[:col_mid]
        if char == 'R':
            cols = cols[col_mid:]

    seat_id = rows[0] * 8 + cols[0]
    seats.append(seat_id)
    if seat_id > max_id:
        max_id = seat_id

assert max_id == 855

sorted_seats = sorted(seats)
for i, s in enumerate(sorted_seats):
    if i and sorted_seats[i-1] + 1 != s:
        my_seat = sorted_seats[i-1] + 1

assert my_seat == 552

print("Part 1:", max_id)
print("Part 2:", my_seat)
