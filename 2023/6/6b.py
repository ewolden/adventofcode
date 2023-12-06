import math
with open('6input.txt','r') as f:
    time = int(''.join([x for x in f.readline().split(':')[1].strip().split(' ') if x != '']))
    distance = int(''.join([x for x in f.readline().split(':')[1].strip().split(' ')  if x != '']))

    lower_bound = math.floor((time - math.sqrt(pow(time, 2) - 4 * distance))/2)
    upper_bound = math.ceil((time + math.sqrt(pow(time, 2) - 4 * distance))/2)
    print(upper_bound-lower_bound - 1)

#4 8 9
#n^2 - nd + x = 0