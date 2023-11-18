def find_num_adapters(input_list, current_lower_possibilities, current_joltage):
    toalt_lower_possibilities = current_lower_possibilities
    for index, adapter in enumerate(input_list):
        if adapter <= current_joltage + 3:
            toalt_lower_possibilities = toalt_lower_possibilities + find_num_adapters(input_list[index:],current_lower_possibilities, current_joltage)
        else:
            break
    return toalt_lower_possibilities


adapters = []
with open('input_shortest.txt','r') as f:
    for line in f:
        adapters.append(int(line.strip()))

phone_rating = max(adapters) + 3
adapters.sort()

previous_adapter = 0
#for adapter in adapters:
#    print(adapter)

print(find_num_adapters(adapters,0, 0))