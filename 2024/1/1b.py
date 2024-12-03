import re
left_list = []
right_list = []
with open('1input.txt','r') as f:
    for line in f:
        all_nums = re.findall('\d+', line)
        left_list.append(int(all_nums[0]))
        right_list.append(int(all_nums[1]))

similarity_score = 0

for left_num in left_list:
    occurences = 0
    for right_num in right_list:
        if left_num == right_num:
            occurences += 1
    similarity_score += left_num * occurences
print(similarity_score)