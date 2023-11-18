gamma_rate = 0
epsilon_rate = 0

current_zeros = []
current_ones = []
most_common_bit = []

with open('3input.txt','r') as f:
    for line in f:
        if current_ones == [] and current_zeros == []:
            current_zeros = [0] * (len(line.strip()))
            current_ones = [0] * (len(line.strip()))
            most_common_bit = [0] * (len(line.strip()))
        for index, value in enumerate(line.strip()):
            if int(value) == 0:
                current_zeros[index] += 1
            else:
                current_ones[index] += 1



for index, value in enumerate(current_ones):
    if value > current_zeros[index]:
        most_common_bit[index] = '1'
    else:
        most_common_bit[index] = '0'
print(''.join(most_common_bit))
print(''.join('1' if x == '0' else '0' for x in ''.join(most_common_bit)))
gamma_rate = int(''.join(most_common_bit),2)
epsilon_rate = int(''.join('1' if x == '0' else '0' for x in ''.join(most_common_bit)),2)
print(gamma_rate * epsilon_rate)
#print(num_increases + 1)