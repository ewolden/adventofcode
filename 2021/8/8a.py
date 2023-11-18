
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
    

num_numbers = 0
with open('8input.txt','r') as f:
    for line in f:
        for digit in line.split(' | ')[1].split(' '):
            found, value = find_number(digit.strip())
            if found:
                num_numbers += 1
print(num_numbers)