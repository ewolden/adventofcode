total_pairs = 0
with open('4input.txt','r') as f:
    for line in f:
        tasks = line.rstrip().split(',')
        first_elf = tasks[0].split('-')
        second_elf = tasks[1].split('-')
        if (int(first_elf[1]) - int(second_elf[1]) >= 0 and int(first_elf[0]) - int(second_elf[0]) <= 0) \
            or (int(second_elf[1]) - int(first_elf[1]) >= 0 and int(second_elf[0]) - int(first_elf[0]) <= 0):
            total_pairs = total_pairs + 1
print(total_pairs)