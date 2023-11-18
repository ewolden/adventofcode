current_fish = []
with open('6input.txt','r') as f:
    for line in f:
        current_fish = [int(x) for x in line.strip().split(',')]

num_fish_per_day = {}
for i in current_fish:
    num_fish_per_day[i] = num_fish_per_day[i]+1 if i in num_fish_per_day else 1
for i in range(256):
    new_fish = {}
    for fish in num_fish_per_day:
        if fish == 0:
            new_fish[8] = num_fish_per_day[fish]
            new_fish[6] = num_fish_per_day[fish]+new_fish[6] if 6 in new_fish else num_fish_per_day[fish]
        else:
            new_fish[fish-1] = num_fish_per_day[fish]+new_fish[fish-1] if fish-1 in new_fish else num_fish_per_day[fish]
    num_fish_per_day = new_fish.copy()
print(sum(num_fish_per_day.values()))