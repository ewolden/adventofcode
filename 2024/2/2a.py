with open('2input.txt','r') as f:
    safe_reports = 0
    for line in f:
        previous_num = 0
        increasing = True
        safe = True
        for idx, num in enumerate(line.split()):
            current_num = int(num)
            if idx == 0:
                previous_num = current_num
                continue

            if not (abs(previous_num - current_num) <= 3 and abs(previous_num - current_num) >= 1):
                safe = False
                break

            if idx == 1:
                increasing = True if previous_num < current_num else False
                previous_num = current_num
                continue
            
            if not ((increasing and previous_num < current_num) or\
                (not increasing and previous_num > current_num)):
                safe = False
                break

            previous_num = current_num

        safe_reports += 1 if safe else 0

print(safe_reports)
        