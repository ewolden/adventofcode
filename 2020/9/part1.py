def find_sum(number_to_find, last_20_numbers):
    for num1 in last_20_numbers:
        for num2 in last_20_numbers:
            if num1 != num2:
                if num1 + num2 == number_to_find:
                    return True
    return False

last_20 = []

with open('input.txt','r') as f:
    for line in f:
        if len(last_20) < 25:
            last_20.append(int(line.strip()))
        else:
            if not find_sum(int(line.strip()), last_20):
                print(int(line.strip()))
                break
            last_20.append(int(line.strip()))
            last_20.pop(0)