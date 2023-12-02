import re
sum_all = 0
with open('1input.txt','r') as f:
    for line in f:
        all_nums = re.findall('\d', line)
        output = int(str(all_nums[0]) + str(all_nums[-1]))
        sum_all += output
print(sum_all)
