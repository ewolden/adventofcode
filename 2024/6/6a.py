import re

def vertical_slices(matrix):
    return [''.join(list(col)) for col in zip(*matrix)]

def find_guard(map):
    for idx, row in enumerate(map):
        match = re.findall(r'\<|\>|\^|v', row)
        if match:
            return (match[0], (idx, row.index(match[0])))

def move_guard(map, start_position, tracked_path = []):
    if start_position[0] == '<':
        distance = map[start_position[1][0]][:start_position[1][1]][::-1].find('#')
        for i in range(distance):
            tracked_path.append((start_position[1][0], start_position[1][1] - i))
        if distance == -1:
            for i in range(len(map[start_position[1][0]][:start_position[1][1]][::-1])):
                tracked_path.append((start_position[1][0], start_position[1][1] - i))
            return tracked_path
        return move_guard(map, ('^', (start_position[1][0], start_position[1][1] - distance)), tracked_path)
    
    elif start_position[0] == '>':
        distance = map[start_position[1][0]][start_position[1][1]:].find('#') - 1
        for i in range(distance):
            tracked_path.append((start_position[1][0], start_position[1][1] + i))
        if distance == -2:
            for i in range(len(map[start_position[1][0]][start_position[1][1]:])):
                tracked_path.append((start_position[1][0], start_position[1][1] + i))
            return tracked_path
        return move_guard(map, ('v', (start_position[1][0], start_position[1][1] + distance)), tracked_path)
    
    elif start_position[0] == '^':
        vertical_map = vertical_slices(map)
        distance = vertical_map[start_position[1][1]][:start_position[1][0]][::-1].find('#')
        for i in range(distance):
                tracked_path.append((start_position[1][0] - i, start_position[1][1]))
        if distance == -1:
            for i in range(len(vertical_map[start_position[1][1]][:start_position[1][0]][::-1])):
                tracked_path.append((start_position[1][0] - i, start_position[1][1]))
            return tracked_path
        return move_guard(map, ('>', (start_position[1][0] - distance, start_position[1][1])), tracked_path)
    
    elif start_position[0] == 'v':
        vertical_map = vertical_slices(map)
        distance = vertical_map[start_position[1][1]][start_position[1][0]:].find('#') - 1
        for i in range(distance):
                tracked_path.append((start_position[1][0] + i, start_position[1][1]))
        if distance == -2:
            for i in range(len(vertical_map[start_position[1][1]][start_position[1][0]:])):
                tracked_path.append((start_position[1][0] + i, start_position[1][1]))
            return tracked_path
        return move_guard(map, ('<', (start_position[1][0] + distance, start_position[1][1])), tracked_path)
    

        


map = []
with open('6input.txt','r') as f:
    for line in f:
        map.append(line.strip())

print(len(list(set(move_guard(map, find_guard(map))))))