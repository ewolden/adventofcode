lines = [[0] * 1000 for i in range(1000)]
with open('5input.txt','r') as f:
    for line in f:
        x1, y1 = line.strip().split(' -> ')[0].split(',')
        x2, y2 = line.strip().split(' -> ')[1].split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if y1 == y2:
            lines[y1][x1] += 1
            while x1 != x2:
                if x1 > x2:
                    x1 -= 1
                else:
                    x1 += 1
                lines[y1][x1] += 1
        elif x1 == x2:
            lines[y1][x1] += 1
            while y1 != y2:
                if y1 > y2:
                    y1 -= 1
                else:
                    y1 += 1
                lines[y1][x1] += 1
number_of_crosses = 0
for line in lines:
    for number in line:
        if number >= 2:
            number_of_crosses += 1
print(number_of_crosses)