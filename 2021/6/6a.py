current_fish = []
with open('6input.txt','r') as f:
    for line in f:
        current_fish = [int(x) for x in line.strip().split(',')]

new_fish = []
for i in range(80):
    for idx, fish in enumerate(current_fish):
        if fish == 0:
            current_fish[idx] = 6
            new_fish.append(8)
        else:
            current_fish[idx] -= 1
    current_fish = current_fish + new_fish.copy()
    new_fish = []
print(len(current_fish))