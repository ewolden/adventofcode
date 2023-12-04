def is_digit(char):
    if char in '0123456789':
        return True
    else:
        return False

def find_number(arr, line_idx, idx):
    i = idx
    number = []
    while i <= len(arr[line_idx])-1 and is_digit(arr[line_idx][i]):
        number.append(arr[line_idx][i])
        i += 1
    i = idx - 1
    while i >= 0 and is_digit(arr[line_idx][i]):
        number = [arr[line_idx][i]] + number
        i -= 1
    return int(''.join(number))

def find_adjacent(arr, line_idx, idx):
    adjecent_nums = []
    num_adjacent = 0
    #row -1
    if line_idx > 0:
        if idx > 0 and is_digit(arr[line_idx-1][idx-1]) and is_digit(arr[line_idx-1][idx+1]) and not is_digit(arr[line_idx-1][idx]):
            adjecent_nums.append(find_number(arr, line_idx-1, idx-1))
            adjecent_nums.append(find_number(arr, line_idx-1, idx+1))
        elif idx > 0 and is_digit(arr[line_idx-1][idx-1]):
            adjecent_nums.append(find_number(arr, line_idx-1, idx-1))
        elif is_digit(arr[line_idx-1][idx]):
            adjecent_nums.append(find_number(arr, line_idx-1, idx))
        elif idx < len(arr[line_idx])-1 and is_digit(arr[line_idx-1][idx+1]):
            adjecent_nums.append(find_number(arr, line_idx-1, idx+1))
    #same row
    if idx > 0 and is_digit(arr[line_idx][idx-1]):
        adjecent_nums.append(find_number(arr, line_idx, idx-1))
    if idx < len(arr[line_idx])-1 and is_digit(arr[line_idx][idx+1]):
        adjecent_nums.append(find_number(arr, line_idx, idx+1))
    #row +1
    if line_idx < len(arr) -1:
        if idx > 0 and is_digit(arr[line_idx+1][idx-1]) and is_digit(arr[line_idx+1][idx+1]) and not is_digit(arr[line_idx+1][idx]):
            adjecent_nums.append(find_number(arr, line_idx+1, idx-1))
            adjecent_nums.append(find_number(arr, line_idx+1, idx+1))
        elif idx > 0 and is_digit(arr[line_idx+1][idx-1]):
            adjecent_nums.append(find_number(arr, line_idx+1, idx-1))
        elif is_digit(arr[line_idx+1][idx]):
            adjecent_nums.append(find_number(arr, line_idx+1, idx))
        elif idx < len(arr[line_idx])-1 and is_digit(arr[line_idx+1][idx+1]):
            adjecent_nums.append(find_number(arr, line_idx+1, idx+1))
    if len(adjecent_nums) == 2:
        return adjecent_nums
    #else:
    #    return []

full_arr = []
with open('3input.txt','r') as f:
    for line in f:
        full_arr.append(line.strip())


total_nums = 0
in_digit = False
cur_num_has_adjacent =  False
start_digit_idx = 0
for line_idx, line in enumerate(full_arr):
    in_digit = False
    cur_num_has_adjacent =  False
    for idx, char in enumerate(line):
        if char == '*':
            adjacents_found = find_adjacent(full_arr, line_idx, idx)
            if adjacents_found:
                total_nums += adjacents_found[0] * adjacents_found[1]
print(total_nums)