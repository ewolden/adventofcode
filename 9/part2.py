def find_sum(number_to_find, last_20_numbers):
    for num1 in last_20_numbers:
        for num2 in last_20_numbers:
            if num1 != num2:
                if num1 + num2 == number_to_find:
                    return True
    return False

def find_contigous_number(number_to_find, input_list, current_low_index):
    smallest_index = current_low_index
    largest_index = 0
    found_num = False
    current_sum = 0
    for index, number in enumerate(input_list):
        current_sum = current_sum + number
        if current_sum == number_to_find:
            #print(smallest_index, smallest_index + index)
            largest_index = smallest_index + index
            found_num = True
    if not found_num:
        #print(number_to_find, input_list[1:])
        inner_found_num, smallest_index, largest_index = find_contigous_number(number_to_find, input_list[1:], current_low_index + 1)
        if inner_found_num:
            return inner_found_num, smallest_index, largest_index
    return found_num, smallest_index, largest_index

complete_list = []

with open('input.txt','r') as f:
    for line in f:
        complete_list.append(int(line.strip()))

found, low_idx, high_idx = find_contigous_number(756008079, complete_list, 0)
print(found, low_idx, high_idx, min(complete_list[low_idx:high_idx]) + max(complete_list[low_idx:high_idx]))
#print(find_contigous_number(756008079, complete_list))