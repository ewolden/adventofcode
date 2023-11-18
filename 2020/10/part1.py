adapters = []
with open('input.txt','r') as f:
    for line in f:
        adapters.append(int(line.strip()))

phone_rating = max(adapters) + 3
adapters.sort()

joltage_differences = [[],[],[],[]]
previous_adapter = 0
for adapter in adapters:
    joltage_differences[adapter - previous_adapter].append(1)
    previous_adapter = adapter
joltage_differences[phone_rating - previous_adapter].append(1)
for jolt_diff in joltage_differences:
    print(len(jolt_diff))

print(len(joltage_differences[1])*len(joltage_differences[3]))