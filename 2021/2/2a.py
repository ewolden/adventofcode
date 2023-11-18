current_depth = 0
current_x = 0
num_increases = 0
with open('2input.txt','r') as f:
    for line in f:
        command, value = line.strip().split(' ')
        value = int(value)
        if command == 'down':
            current_depth += value
        elif command == 'up':
            current_depth -= value
        elif command == 'forward':
            current_x += value
print(current_x * current_depth)