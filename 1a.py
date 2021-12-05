previous_value = None
num_increases = 0
with open('1input.txt','r') as f:
    for line in f:
        if previous_value and line > previous_value:
            num_increases += 1
        previous_value = line
print(num_increases + 1)