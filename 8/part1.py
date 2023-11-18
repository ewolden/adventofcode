instruction_list = []
with open('input.txt', 'r') as f:
    for line in f:
        instruction_list.append(line.strip().split(' '))
#print(instruction_list)

visited_instructions = []
current_index = 0
current_acc = 0
while current_index not in visited_instructions:
    visited_instructions.append(current_index)
    #print(instruction_list[current_index], "index", current_index, "acc", current_acc)
    if instruction_list[current_index][0] == 'nop':
        current_index = current_index + 1
    elif instruction_list[current_index][0] == 'acc':
        if instruction_list[current_index][1][0] == '+':
            current_acc = current_acc + int(instruction_list[current_index][1][1:])
        elif instruction_list[current_index][1][0] == '-':
            current_acc = current_acc - int(instruction_list[current_index][1][1:])
        current_index = current_index + 1
    elif instruction_list[current_index][0] == 'jmp':
        if instruction_list[current_index][1][0] == '+':
            current_index = current_index + int(instruction_list[current_index][1][1:])
        elif instruction_list[current_index][1][0] == '-':
            current_index = current_index - int(instruction_list[current_index][1][1:])
print(current_acc)