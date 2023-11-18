import math
monkeys = []
monkeys_items = []

with open('11input.txt','r') as f:
    
    while True:
        first_line = f.readline()
        if first_line == '':
            break
        monkey_number = int(first_line[7])
        monkey_items = [int(x) for x in f.readline().rstrip()[18:].split(', ')]
        monkey_operation = f.readline().rstrip()[19:]
        monkey_test = int(f.readline().rstrip()[21:])
        monkey_true = int(f.readline().rstrip()[-1])
        monkey_false = int(f.readline().rstrip()[-1])
        current_monkey = {
            'number': monkey_number,
            'operation': monkey_operation,
            'test': monkey_test,
            'true': monkey_true,
            'false': monkey_false
        }
        monkeys.append(current_monkey)
        monkeys_items.append(monkey_items.copy())
        f.readline()

monkeys_inspected_item = [0] * len(monkeys)
for round in range(20):
    for idx, monkey in enumerate(monkeys):
        while len(monkeys_items[idx]) > 0:
            current_item = monkeys_items[idx].pop(0)
            old = current_item
            current_item = math.floor(eval(monkey['operation']) / 3)
            if current_item % monkey['test'] == 0:
                monkeys_items[monkey['true']].append(current_item)
            else:
                monkeys_items[monkey['false']].append(current_item)
            monkeys_inspected_item[idx] = monkeys_inspected_item[idx] + 1
highest = monkeys_inspected_item.pop(monkeys_inspected_item.index(max(monkeys_inspected_item)))
second_highest = monkeys_inspected_item.pop(monkeys_inspected_item.index(max(monkeys_inspected_item)))
print(highest*second_highest)
