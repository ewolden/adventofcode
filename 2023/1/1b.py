import re
sum_all = 0
regex_string = 'one|two|three|four|five|six|seven|eight|nine'
full_regex_string = '(?=(\d'+ '|' + regex_string + '))'
with open('1input.txt','r') as f:
    for line in f:
        all_nums = re.findall(full_regex_string, line)
        if all_nums[0] in regex_string.split('|'):
            if all_nums[0] == 'one': all_nums[0] = 1
            if all_nums[0] == 'two': all_nums[0] = 2
            if all_nums[0] == 'three': all_nums[0] = 3
            if all_nums[0] == 'four': all_nums[0] = 4
            if all_nums[0] == 'five': all_nums[0] = 5
            if all_nums[0] == 'six': all_nums[0] = 6
            if all_nums[0] == 'seven': all_nums[0] = 7
            if all_nums[0] == 'eight': all_nums[0] = 8
            if all_nums[0] == 'nine': all_nums[0] = 9
            #if all_nums[0] == 'zero': all_nums[0] = 0
        if all_nums[-1] in regex_string.split('|'):
            if all_nums[-1] == 'one': all_nums[-1] = 1
            if all_nums[-1] == 'two': all_nums[-1] = 2
            if all_nums[-1] == 'three': all_nums[-1] = 3
            if all_nums[-1] == 'four': all_nums[-1] = 4
            if all_nums[-1] == 'five': all_nums[-1] = 5
            if all_nums[-1] == 'six': all_nums[-1] = 6
            if all_nums[-1] == 'seven': all_nums[-1] = 7
            if all_nums[-1] == 'eight': all_nums[-1] = 8
            if all_nums[-1] == 'nine': all_nums[-1] = 9
            #if all_nums[-1] == 'zero': all_nums[-1] = 0
        output = int(str(all_nums[0]) + str(all_nums[-1]))
        sum_all += output
print(sum_all)