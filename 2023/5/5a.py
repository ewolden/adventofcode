input = []
current_idx = 0
with open('5input.txt','r') as f:
    input.append([int(x) for x in f.readline().replace('  ',' ').strip().split(': ')[1].split(' ')])
    seed_length = len(input[0])
    for line in f:
        current_line = line.replace(' ', ' ').strip()
        if current_line == '':
            if current_idx > 0:
                for idx, value in enumerate(input[current_idx-1]):
                    if input[current_idx][idx] == None:
                        input[current_idx][idx] = value
            current_idx += 1
            input.append([None] * seed_length)
            continue
        if not current_line[0].isdigit(): continue
        current_map = [int(x) for x in current_line.split(' ')]
        for idx, num in enumerate(input[current_idx-1]):
            if num >= current_map[1] and num < current_map[1] + current_map[2]:
                input[current_idx][idx] = current_map[0] + num - current_map[1]

for idx, value in enumerate(input[current_idx-1]):
    if input[current_idx][idx] == None:
        input[current_idx][idx] = value
print(min(input[-1]))