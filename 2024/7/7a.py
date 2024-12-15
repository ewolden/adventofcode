import itertools

def check_if_solvable(equation):
    possible_signs = []
    for combination in itertools.product('+*', repeat=len(equation[1])):
        possible_signs.append(''.join(combination))
    possible_signs = list(set(possible_signs))

    for signs in possible_signs:
        current_value = equation[1][0]
        for i in range(len(equation[1]) - 1):
            current_value = eval(str(current_value) + signs[i] + str(equation[1][i+1]))
        if current_value == equation[0]:
            return True
    return False


equations = []
with open('7input.txt', 'r') as f:
    for line in f:
        equations.append((int(line.strip().split(': ')[0]),[int(x) for x in line.strip().split(': ')[1].split(' ')]))

total_sum = 0
for eq in equations:
    if check_if_solvable(eq):
        total_sum += eq[0]
print(total_sum)