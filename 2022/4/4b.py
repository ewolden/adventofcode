total_pairs = 0
elfs = []
with open('4input.txt','r') as f:
    for line in f:
        tasks = line.rstrip().split(',')
        first_elf = tasks[0].split('-')
        second_elf = tasks[1].split('-')

        for i in range(int(first_elf[0]), int(first_elf[1])+1):
            if i in range(int(second_elf[0]), int(second_elf[1])+1):
                total_pairs = total_pairs + 1
                break


print(total_pairs)