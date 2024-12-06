import re
sum_of_multiplications = 0
with open('3input.txt','r') as f:
    multiply = True
    for line in f:
        matches = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
        for instruction in matches:
            if instruction == 'do()':
                multiply = True
            elif instruction == 'don\'t()':
                multiply = False
            elif multiply:
                multinumbers = [int(x) for x in re.findall('\d+', instruction)]
                sum_of_multiplications += multinumbers[0] * multinumbers[1]

            
print(sum_of_multiplications)