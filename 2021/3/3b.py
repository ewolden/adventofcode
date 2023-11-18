gamma_rate = 0
epsilon_rate = 0
oxygen_generator_rating = []
co2_scrubber_rating = []

current_zeros = []
current_ones = []
most_common_bit = []
all_lines = []

def find_mcb(input, index):
    c0 = 0
    c1 = 0
    for value in input:
        if value[index] == '0':
            c0 += 1
        else:
            c1 += 1
    answer = '1'
    if c0 > c1:
        answer = '0'
    return answer, c0 == c1

with open('3input.txt','r') as f:
    for line in f:
        all_lines.append(list(line.strip()))
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
least_common_bit = ''.join('1' if x == '0' else '0' for x in ''.join(most_common_bit))
oxygen_generator_rating = all_lines.copy()
co2_scrubber_rating = all_lines.copy()
current_bit_index = 0
indexes_to_delete = []
while len(oxygen_generator_rating) > 1:
    next_mcb, mcb_equals = find_mcb(oxygen_generator_rating, current_bit_index)
    for index, value in enumerate(oxygen_generator_rating):
        if value[current_bit_index] != next_mcb or (value[current_bit_index] == '0' and mcb_equals):
            indexes_to_delete.append(index)
    indexes_to_delete.sort(reverse=True)
    for index in indexes_to_delete:
        oxygen_generator_rating.pop(index)
    indexes_to_delete = []
    current_bit_index += 1
    
print(int(''.join(oxygen_generator_rating[0]),2))

current_bit_index = 0
indexes_to_delete = []
while len(co2_scrubber_rating) > 1:
    
    next_mcb, mcb_equals = find_mcb(co2_scrubber_rating, current_bit_index)
    for index, value in enumerate(co2_scrubber_rating):
        if value[current_bit_index] == next_mcb or (value[current_bit_index] != '0' and mcb_equals):
            indexes_to_delete.append(index)
    indexes_to_delete.sort(reverse=True)
    for index in indexes_to_delete:
        co2_scrubber_rating.pop(index)
    indexes_to_delete = []
    current_bit_index += 1
    
print(int(''.join(co2_scrubber_rating[0]),2))
#print(''.join(most_common_bit))
print(int(''.join(oxygen_generator_rating[0]),2) * int(''.join(co2_scrubber_rating[0]),2))
#print(gamma_rate * epsilon_rate)
#print(num_increases + 1)