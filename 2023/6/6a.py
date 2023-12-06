import math
with open('6input.txt','r') as f:
    times = [x for x in f.readline().split(':')[1].strip().split(' ') if x != '']
    distances = [x for x in f.readline().split(':')[1].strip().split(' ')  if x != '']
    answer = 1
    for idx, t in enumerate(times):
        lower_bound = math.floor(((int(t) - math.sqrt(pow(int(t), 2) - 4 * (int(distances[idx]))))/2))
        upper_bound = math.ceil((int(t) + math.sqrt(pow(int(t), 2) - 4 * (int(distances[idx]))))/2)
        answer *= upper_bound-lower_bound - 1
    print(answer)

#4 8 9
#n^2 - nd + x = 0