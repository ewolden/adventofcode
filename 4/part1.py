def get_keys(line):
    keys = []
    for ele in line.split(' '):
        keys.append(ele.split(':')[0].strip())
    return keys

def passport_validity(passport):
    if len(passport) == 7 and 'cid' not in passport:
        return True
    elif len(passport) == 8:
        return True
    else:
        return False

valid_passports = 0
with open('input.txt', 'r') as f:
    passport = []
    for line in f:
        print("----", line)
        if line.strip() == '':
            print(passport)
            if passport_validity(passport):
                valid_passports = valid_passports + 1
            passport = []
        else:
            passport = passport + get_keys(line)
    if passport_validity(passport):
                valid_passports = valid_passports + 1
print(valid_passports)