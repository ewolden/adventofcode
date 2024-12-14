import re

def vertical_slices(matrix):
    return [''.join(list(col)) for col in zip(*matrix)]

def find_guard(map):
    for idx, row in enumerate(map):
        match = re.findall(r'\<|\>|\^|v', row)
        if match:
            return (match[0], (idx, row.index(match[0])))

def move_guard(map, start_position, tracked_path = None, iteration = 0):
    if tracked_path is None:
        tracked_path = []
    if iteration > 200: # arbitrary number to prevent infinite loops, but high enough to allow for the guard to move around the map
        return tracked_path, True
    if start_position[0] == '<':
        distance = map[start_position[1][0]][:start_position[1][1]][::-1].find('#')
        for i in range(distance):
            tracked_path.append((start_position[1][0], start_position[1][1] - i))
        if distance == -1:
            for i in range(len(map[start_position[1][0]][:start_position[1][1]][::-1])):
                tracked_path.append((start_position[1][0], start_position[1][1] - i))
            return tracked_path, False
        return move_guard(map, ('^', (start_position[1][0], start_position[1][1] - distance)), tracked_path, iteration + 1)
    
    elif start_position[0] == '>':
        distance = map[start_position[1][0]][start_position[1][1]:].find('#') - 1
        if distance == -1:
            return move_guard(map, ('v', (start_position[1][0], start_position[1][1])), tracked_path, iteration + 1)
        for i in range(distance):
            tracked_path.append((start_position[1][0], start_position[1][1] + i))
        if distance == -2:
            for i in range(len(map[start_position[1][0]][start_position[1][1]:])):
                tracked_path.append((start_position[1][0], start_position[1][1] + i))
            return tracked_path, False
        return move_guard(map, ('v', (start_position[1][0], start_position[1][1] + distance)), tracked_path, iteration + 1)
    
    elif start_position[0] == '^':
        vertical_map = vertical_slices(map)
        distance = vertical_map[start_position[1][1]][:start_position[1][0]][::-1].find('#')
        for i in range(distance):
                tracked_path.append((start_position[1][0] - i, start_position[1][1]))
        if distance == -1:
            for i in range(len(vertical_map[start_position[1][1]][:start_position[1][0]][::-1])):
                tracked_path.append((start_position[1][0] - i, start_position[1][1]))
            return tracked_path, False
        return move_guard(map, ('>', (start_position[1][0] - distance, start_position[1][1])), tracked_path, iteration + 1)
    
    elif start_position[0] == 'v':
        vertical_map = vertical_slices(map)
        distance = vertical_map[start_position[1][1]][start_position[1][0]:].find('#') - 1
        if distance == -1:
            return move_guard(map, ('<', (start_position[1][0], start_position[1][1])), tracked_path, iteration + 1)
        for i in range(distance):
                tracked_path.append((start_position[1][0] + i, start_position[1][1]))
        if distance == -2:
            for i in range(len(vertical_map[start_position[1][1]][start_position[1][0]:])):
                tracked_path.append((start_position[1][0] + i, start_position[1][1]))
            return tracked_path, False
        return move_guard(map, ('<', (start_position[1][0] + distance, start_position[1][1])), tracked_path, iteration + 1)
    

        


map = []
with open('6input.txt', 'r') as f:
    for line in f:
        map.append(line.strip())

start_position = find_guard(map)
complete_route, _ = move_guard(map, start_position)
complete_route = list(set(complete_route))
flipped_map = vertical_slices(map)
num_loops = 0
print(len(complete_route))
for step in complete_route:
    if step == start_position[1]:
        continue
    map_copy = map.copy()
    row_as_list = list(map_copy[step[0]])
    row_as_list[step[1]] = '#'
    map_copy[step[0]] = ''.join(row_as_list)


    _, loops = move_guard(map_copy, start_position)
    if loops:
        num_loops += 1
print(num_loops)