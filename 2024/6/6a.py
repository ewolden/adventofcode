import re

def find_guard(map):
    for idx, row in enumerate(map):
        match = re.findall(r'\<|\>|\^|v', row)
        if match:
            return (match[0], (idx, row.index(match[0])))

def move_guard(map, start_position):
    if start_position[0] == '<':
        map[start_position[1][0]][:start_position[1][1]].rfind('#') # wrong, will not give right index
    elif start_position[0] == '>':

        


map = []
with open('6sampleinput.txt','r') as f:
    for line in f:
        map.append(line.strip())



print(find_guard(map)) 