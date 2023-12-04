def is_digit(char):
    if char in '0123456789':
        return True
    else:
        return False
    
def has_adjacent(arr, line_idx, idx):
    if line_idx > 0:
        if (idx > 0 and is_digit(arr[line_idx-1][idx-1])) \
            or (is_digit(arr[line_idx-1][idx])) \
            or (idx < len(arr[0])-1 and is_digit(arr[line_idx-1][idx+1])):
            return True
    if (idx > 0 and is_digit(arr[line_idx][idx-1])) \
        or (idx < len(arr[0])-1 and is_digit(arr[line_idx][idx+1])):
        return True
    if line_idx < len(arr)-1:
        if (idx > 0 and is_digit(arr[line_idx+1][idx-1])) \
            or (is_digit(arr[line_idx+1][idx])) \
            or (idx < len(arr[0])-1 and is_digit(arr[line_idx+1][idx+1])):
            return True
    return False


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
            


            if not cur_num_has_adjacent: cur_num_has_adjacent = has_adjacent(full_arr, line_idx, idx)
            if not in_digit:
                start_digit_idx = idx
                in_digit = True
        elif in_digit:
            digit = int(line[start_digit_idx:idx])
            if digit == 6: print(cur_num_has_adjacent)
            if cur_num_has_adjacent: total_nums += digit
            in_digit = False
            cur_num_has_adjacent = False
    if in_digit and cur_num_has_adjacent:
        digit = int(line[start_digit_idx:len(line)])
        total_nums += digit
print(total_nums)