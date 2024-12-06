def check_saftey(nums, level_removed=False):
    previous_num = 0
    increasing = True
    for idx, current_num in enumerate(nums):
        if idx == 0:
            previous_num = current_num
            continue

        if not (abs(previous_num - current_num) <= 3 and abs(previous_num - current_num) >= 1):
            if level_removed:
                return False
            else:
                safe_with_one_level_removed = []
                for i in range(len(nums)):
                    safe_with_one_level_removed.append(check_saftey(nums[:i] + nums[i+1:], True))
                for safe in safe_with_one_level_removed:
                    if safe:
                        return True
                return False

        if idx == 1:
            increasing = True if previous_num < current_num else False
            previous_num = current_num
            continue
        
        if not ((increasing and previous_num < current_num) or\
            (not increasing and previous_num > current_num)):
            if level_removed:
                return False
            else:
                safe_with_one_level_removed = []
                for i in range(len(nums)):
                    safe_with_one_level_removed.append(check_saftey(nums[:i] + nums[i+1:], True))
                for safe in safe_with_one_level_removed:
                    if safe:
                        return True
                return False

        previous_num = current_num
    return True

with open('2input.txt','r') as f:
    safe_reports = 0
    for line in f:
        safe_reports += 1 if check_saftey([int(x) for x in line.split()]) else 0

print(safe_reports)
        