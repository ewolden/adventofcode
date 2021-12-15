def outer_join(larger, smaller): 
    return ''.join([x for x in larger if x not in smaller])

def find_number(input):
    if len(input) == 2:
        return True, [1]
    elif len(input) == 4:
        return True, [4]
    elif len(input) == 3:
        return True, [7]
    elif len(input) == 7:
        return True, [8]
    return False, []



def find_rest_of_numbers(input, input_finished):
    finished_number = input_finished.copy()
    if input[1] and (not finished_number[2] or not finished_number[5]):
        finished_number[2] = input[1]
        finished_number[5] = input[1]
    if input[1] and input[7]:
        finished_number[0] = outer_join(input[7], input[1])
    if input[1] and input[4] and (not finished_number[1] or not finished_number[3]):
        finished_number[1] = outer_join(input[4], input[1])
        finished_number[3] = outer_join(input[4], input[1])
    if input[1] and input[4] and input[7] and input[8] and (not finished_number[4] or not finished_number[6]):
        finished_number[4] = outer_join(outer_join(input[8], input[7]), outer_join(input[4], input[1]))
        finished_number[6] = outer_join(outer_join(input[8], input[7]), outer_join(input[4], input[1]))
    return finished_number

def find_combinations(input_chars, input_numbers, input_digit_positions):
    tmp_input_numbers = input_numbers.copy()
    tmp_input_digit_positions = input_digit_positions.copy()
    if len(input_chars) == 6 and input_numbers[8]:
        missing_char = outer_join(input_numbers[8], input_chars)
        for idx, char in enumerate(input_digit_positions):
            if missing_char in char:
                if idx == 3:
                    tmp_input_numbers[0] = input_chars
                    tmp_input_digit_positions[idx] = missing_char
                elif idx == 2:
                    tmp_input_numbers[6] = input_chars
                    tmp_input_digit_positions[idx] = missing_char
                elif idx == 4:
                    tmp_input_numbers[6] = input_chars
                    tmp_input_digit_positions[idx] = missing_char
                
    return tmp_input_numbers, tmp_input_digit_positions

def return_number(input, input_finished):
    final_number_idx = [0] * 7
    for idx, char in enumerate(input_finished):
        if char in input:
            final_number_idx[idx] = 1
    if final_number_idx == [1,1,1,0,1,1,1]:
        return 0
    elif final_number_idx == [0,0,1,0,0,1,0]:
        return 1
    elif final_number_idx == [1,0,1,1,1,0,1]:
        return 2
    elif final_number_idx == [1,0,1,1,0,1,1]:
        return 3
    elif final_number_idx == [0,1,1,1,0,1,0]:
        return 4
    elif final_number_idx == [1,1,0,1,0,1,1]:
        return 5
    elif final_number_idx == [1,1,0,1,1,1,1]:
        return 6
    elif final_number_idx == [1,0,1,0,0,1,0]:
        return 7
    elif final_number_idx == [1,1,1,1,1,1,1]:
        return 8
    elif final_number_idx == [1,1,1,1,0,1,1]:
        return 9




digit_list = []
total_sum = 0
with open('8input.txt','r') as f:
    for line in f:
        digit_list.append(line.strip().replace(' |', '').split(' '))

for line in digit_list:
    input_numbers = [''] * 10
    for number in line:
        found, value = find_number(number)
        if found:
            input_numbers[value[0]] = number
    input_finished = [''] * 7
    input_finished = find_rest_of_numbers(input_numbers, input_finished)
    for number in line:
        input_numbers, input_finished = find_combinations(number, input_numbers, input_finished)
    input_finished[5] = outer_join(input_finished[5], input_finished[2])
    input_finished[6] = outer_join(input_finished[6], input_finished[4])
    input_finished[1] = outer_join(input_finished[1], input_finished[3])

    number_str = ''
    for number in line[-4:]:
        number_str += str(return_number(number, ''.join(input_finished)))
    total_sum += int(number_str)
print(total_sum)