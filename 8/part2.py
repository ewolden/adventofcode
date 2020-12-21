def try_to_find_end(inst_list, idx, max_length, tmp_acc, tmp_visited_inst):
    visited_inst = tmp_visited_inst.copy()
    acc = tmp_acc
    while idx not in visited_inst and idx < max_length:
        visited_inst.append(idx)
        #print("inner", inst_list[idx], "index", idx, "acc", acc)
        if inst_list[idx][0] == 'nop':
            idx = idx + 1
        elif inst_list[idx][0] == 'acc':
            if inst_list[idx][1][0] == '+':
                acc = acc + int(inst_list[idx][1][1:])
            elif inst_list[idx][1][0] == '-':
                acc = acc - int(inst_list[idx][1][1:])
            idx = idx + 1
        elif inst_list[idx][0] == 'jmp':
            if inst_list[idx][1][0] == '+':
                idx = idx + int(inst_list[idx][1][1:])
            elif inst_list[idx][1][0] == '-':
                idx = idx - int(inst_list[idx][1][1:])
    if idx == max_length:
        return True, acc
    else:
        return False, acc

instruction_list = []
with open('input.txt', 'r') as f:
    for line in f:
        instruction_list.append(line.strip().split(' '))
#print(instruction_list)


max_length = len(instruction_list)
visited_instructions = []
current_index = 0
current_acc = 0
found_end = False
final_acc = 0

while current_index not in visited_instructions and not found_end:
    visited_instructions.append(current_index)
    print(visited_instructions)
    print(instruction_list[current_index], "index", current_index, "acc", current_acc)
    if instruction_list[current_index][0] == 'nop':
        if instruction_list[current_index][1][0] == '+':
            found_end, final_acc = try_to_find_end(instruction_list, current_index + int(instruction_list[current_index][1][1:]), max_length, current_acc, visited_instructions)
        elif instruction_list[current_index][1][0] == '-':
            found_end, final_acc = try_to_find_end(instruction_list, current_index + int(instruction_list[current_index][1][1:]), max_length, current_acc, visited_instructions)
        current_index = current_index + 1
    elif instruction_list[current_index][0] == 'acc':
        if instruction_list[current_index][1][0] == '+':
            current_acc = current_acc + int(instruction_list[current_index][1][1:])
        elif instruction_list[current_index][1][0] == '-':
            current_acc = current_acc - int(instruction_list[current_index][1][1:])
        current_index = current_index + 1
    elif instruction_list[current_index][0] == 'jmp':
        found_end, final_acc = try_to_find_end(instruction_list, current_index + 1, max_length, current_acc, visited_instructions)
        if instruction_list[current_index][1][0] == '+':
            current_index = current_index + int(instruction_list[current_index][1][1:])
        elif instruction_list[current_index][1][0] == '-':
            current_index = current_index - int(instruction_list[current_index][1][1:])
    #print(current_index)
print(found_end)
print(final_acc)