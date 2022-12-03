total_priority = 0
with open('3input.txt','r') as f:
    for line in f:
        num_items = int(len(line.rstrip())/2)
        for item in line[:num_items]:
            if item in line[num_items:]:
                if ord(item) - 96 < 0: 
                    ## uppercase
                    total_priority = total_priority + ord(item) - 64 + 26
                else:
                    ## lowercase
                    total_priority = total_priority + ord(item) - 96
                break
print(total_priority)