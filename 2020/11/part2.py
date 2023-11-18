def adjecent_occupied(seats, index_x, index_y):
    num_occupied = 0
    for row_index, row in enumerate(seats[index_y-1:index_y+2]):
        for seat_index, seat in enumerate(row[index_x-1:index_x+2]):
            if row_index != 1 or seat_index != 1:
                if seat == '#':
                    num_occupied += 1
    return num_occupied

def get_first_seat_in_view(seats, start, direction):
    still_in_floorplan = True
    current_location = start.copy()
    while still_in_floorplan:
        current_location[0] += direction[0]
        current_location[1] += direction[1]
        if current_location[0] < 0 or current_location[0] >= len(seats[0]) or current_location[1] < 0 or current_location[1] >= len(seats):
            return '.'
        if seats[current_location[1]][current_location[0]] == 'L':
            return 'L'
        elif seats[current_location[1]][current_location[0]] == '#':
            return '#'

def sight_adjacent_occupied(seats, index_x, index_y):
    num_occupied = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                if get_first_seat_in_view(seats, [index_x, index_y], [i,j]) == '#':
                    num_occupied += 1
    return num_occupied

def find_new_arrangement(seating_arrangement):
    seat_row_length = len(seating_arrangement[0])
    new_arrangement = []#seating_arrangement.copy()
    new_arrangement.append(''.join(['.'] * seat_row_length))
    for row_index, seat_row in enumerate(seating_arrangement):
        if row_index == 0 or row_index == len(seating_arrangement) - 1:
            continue
        new_arrangement.append('')
        for seat_index, seat in enumerate(seat_row):
            if seat_index == 0 or seat_index == len(seat_row) - 1:
                new_arrangement[row_index] += seat
                continue
            if seat == 'L':
                if not sight_adjacent_occupied(seating_arrangement, seat_index, row_index):
                    seat = '#'
            elif seat == '#':
                if sight_adjacent_occupied(seating_arrangement, seat_index, row_index) >= 5:
                    seat = 'L'
            new_arrangement[row_index] += seat
    new_arrangement.append(''.join(['.'] * seat_row_length))
    return new_arrangement

seats_status = []
seat_row_length = 0
with open('input.txt','r') as f:
    for line in f:
        if seat_row_length == 0:
            seat_row_length = len(line.strip())
            seats_status.append(''.join(['.'] * (seat_row_length + 2)))
        seats_status.append('.' + line.strip() + '.')
seats_status.append(''.join(['.'] * (seat_row_length + 2)))
status_1 = find_new_arrangement(seats_status)

current_seating = seats_status
not_steady = True
while not_steady:
#    print('\n'.join(current_seating))
    next_seating = find_new_arrangement(current_seating)
    if current_seating == next_seating:
        not_steady = False
    current_seating = next_seating.copy()

num_occupied = 0
for row in current_seating:
    for seat in row:
        if seat == '#':
            num_occupied += 1
print(num_occupied)