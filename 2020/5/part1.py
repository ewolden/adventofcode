import math

def find_space(inputline, current_range):
    #FBLR
    #print(inputline, current_range)
    new_range = []
    if inputline[0] in ['F', 'L']:
        new_range = [current_range[0], int(current_range[1] - (current_range[1] - current_range[0] + 1) / 2)]
    elif inputline[0] in ['B', 'R']:
        new_range = [int(current_range[0] + (current_range[1] - current_range[0] + 1) / 2), current_range[1]]
    
    if len(inputline) == 1:
        return new_range
    else:
        return find_space(inputline[1:], new_range)

answers = []
with open('input.txt', 'r') as f:
    for line in f:

        answers.append(find_space(line[:7], [0, 127])[0] * 8 + find_space(line[7:10], [0, 7])[0])
print(max(answers))
        