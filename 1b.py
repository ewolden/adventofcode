previous_window = []
previous_value = None
current_window = []
num_increases = 0
num_reads = 0
with open('1input.txt','r') as f:
    for line in f:
        current_window.append(int(line.strip()))
        if num_reads != 0:
            previous_window.append(previous_value)
        if num_reads >= 3:
            current_window.pop(0)
        if num_reads >= 4:    
            previous_window.pop(0)
            print(current_window)
            print(previous_window)
            if sum(current_window) > sum(previous_window):
                num_increases += 1
        num_reads += 1
        previous_value = int(line.strip())
print(num_increases + 1)