current_depth = 0
current_x = 0
aim = 0
num_increases = 0
with open('2input.txt','r') as f:
    for line in f:
        command, value = line.strip().split(' ')
        value = int(value)
        if command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
        elif command == 'forward':
            current_x += value
            current_depth += aim * value
print(current_x * current_depth)