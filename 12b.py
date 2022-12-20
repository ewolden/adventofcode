import copy
def valid_next(height_array, current_position):
    current_height = height_array[current_position[0]][current_position[1]]
    valid_positions = []
    # left
    next_x = current_position[0] - 1
    next_y = current_position[1]
    if      next_x >= 0 \
        and next_x < len(height_array) \
        and height_array[next_x][next_y] - current_height < 2:
        valid_positions.append([next_x, next_y])
    # right
    next_x = current_position[0] + 1
    next_y = current_position[1]
    if      next_x >= 0 \
        and next_x < len(height_array) \
        and height_array[next_x][next_y] - current_height < 2:
        valid_positions.append([next_x, next_y])
    # up
    next_x = current_position[0] 
    next_y = current_position[1] + 1
    if      next_y >= 0 \
        and next_y < len(height_array[next_x]) \
        and height_array[next_x][next_y] - current_height < 2:
        valid_positions.append([next_x, next_y])
    # down
    next_x = current_position[0]
    next_y = current_position[1] - 1
    if      next_y >= 0 \
        and next_y < len(height_array[next_x]) \
        and height_array[next_x][next_y] - current_height < 2:
        valid_positions.append([next_x, next_y])
    return valid_positions


def dijkstra(height_array, start_position, goal_position, letter_array):
    Q = [(start_position, [], 0)]
    distance_from_source = []

    for line in height_array:
        distance_from_source.append([99999999]*len(line))
    while Q:
        Q.sort(key=lambda a: a[2])
        tree, history, distance = Q.pop(0)
        history += [tree]
        if tree == goal_position:
            new_letter_array = copy.deepcopy(letter_array)
            for segment in history:
                if segment == start_position:
                    continue
                new_letter_array[segment[0]][segment[1]] = new_letter_array[segment[0]][segment[1]].upper()
            for line in new_letter_array:
                print(''.join(line))
            print()
            print(distance-2)#, tree, len(history))
            return distance-2
        neighbours = valid_next(height_array, tree)
        for neighbour in neighbours:
            new_distance = distance + 1
            if new_distance < distance_from_source[neighbour[0]][neighbour[1]]:
                distance_from_source[neighbour[0]][neighbour[1]] = new_distance
                #print(list(filter(lambda x: x[2] == neighbour, Q)))
                if list(filter(lambda x: x[2] == neighbour, Q)) == []:
                    Q.append((copy.deepcopy(neighbour),copy.deepcopy(history),new_distance))
    
height_array = []
letter_array = []
starting_position = []
goal_position = []
with open('12input.txt','r') as f:
    for i, line in enumerate(f):
        current_line = []
        current_letter_line = []
        for j, item in enumerate(line.rstrip()):
            if item == 'S':
                current_line.append(1)
                starting_position = [i, j]
            elif item == 'E':
                current_line.append(27)
                goal_position = [i, j]
            else:
                current_line.append(ord(item) - 96)
            current_letter_line.append(item)
        height_array.append(current_line)
        letter_array.append(current_letter_line)
current_solutions = []
for i, line_position in enumerate(height_array):
    for j, element_position in enumerate(line_position):
        if element_position == 1:
            result = dijkstra(height_array, [i,j], goal_position, letter_array)
            if result is not None:
                current_solutions.append(result)

print(min(current_solutions))