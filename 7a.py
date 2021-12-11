with open('7input.txt','r') as f:
    input = [int(x) for x in f.readline().split(',')]

fuel_calcs = []
for i in range(max(input)):
    fuel_calcs.append(sum([abs(x - i) for x in input]))
print(min(fuel_calcs))