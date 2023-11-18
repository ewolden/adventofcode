total_cals_per_elf = []
with open('1input.txt','r') as f:
    current_elf = 0
    for line in f:
        if line.strip() != '':
            current_elf = current_elf + int(line.strip())
        else:
            total_cals_per_elf.append(current_elf)
            current_elf = 0
total_cals_per_elf.append(current_elf)
total_cals_per_elf.sort(reverse=True)
print(total_cals_per_elf[0] + total_cals_per_elf[1] + total_cals_per_elf[2])