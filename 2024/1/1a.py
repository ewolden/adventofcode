import re
left_list = []
right_list = []
with open('1input.txt','r') as f:
    for line in f:
        all_nums = re.findall('\d+', line)
        left_list.append(int(all_nums[0]))
        right_list.append(int(all_nums[1]))

left_list.sort()
right_list.sort()
distance = 0
for idx, _ in enumerate(left_list):
    distance += abs(left_list[idx] - right_list[idx])
print(distance)