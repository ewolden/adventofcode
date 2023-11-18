total_priority = 0
current_group = []
with open('3input.txt','r') as f:
    for line in f:
        if len(current_group) == 3:
            intersect = set(current_group[0]) & set(current_group[1])
            shared_badge = (intersect & set(current_group[2])).pop()
            if ord(shared_badge) - 96 < 0: 
                ## uppercase
                total_priority = total_priority + ord(shared_badge) - 64 + 26
            else:
                ## lowercase
                total_priority = total_priority + ord(shared_badge) - 96
            current_group = []
            current_group.append(line.rstrip())
        else:
            current_group.append(line.rstrip())
            
intersect = set(current_group[0]) & set(current_group[1])
shared_badge = (intersect & set(current_group[2])).pop()
if ord(shared_badge) - 96 < 0: 
    ## uppercase
    total_priority = total_priority + ord(shared_badge) - 64 + 26
else:
    ## lowercase
    total_priority = total_priority + ord(shared_badge) - 96


print(total_priority)