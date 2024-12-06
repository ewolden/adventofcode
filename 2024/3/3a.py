import re
sum_of_multiplications = 0
with open('3input.txt','r') as f:
    for line in f:
        matches = re.findall('mul\(\d+,\d+\)', line)
        for num in matches:
            multinumbers = [int(x) for x in re.findall('\d+', num)]
            sum_of_multiplications += multinumbers[0] * multinumbers[1]
print(sum_of_multiplications)