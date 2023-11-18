import re

def get_keyValues(line):
    keyValues = dict()
    for ele in line.split(' '):
        keyValues[ele.split(':')[0].strip()] = ele.split(':')[1].strip()
    return keyValues

def passport_validity(passport):
    valid = True
    if (len(passport) == 7 and 'cid' not in passport) or len(passport) == 8:
        print("byr: ", int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002,
            "iyr: ",int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020,
            "eyr: ",int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030,
            "hgt: ",((passport['hgt'][len(passport['hgt']) - 2:] == 'cm' and int(passport['hgt'][:len(passport['hgt']) -2]) >= 150 and int(passport['hgt'][:len(passport['hgt']) -2]) <= 193) or \
            (passport['hgt'][len(passport['hgt']) - 2:] == 'in' and int(passport['hgt'][:len(passport['hgt']) -2]) >= 59 and int(passport['hgt'][:len(passport['hgt']) -2]) <= 76)),
            "hcl: ",re.match('#[0-9a-f]{6}',passport['hcl']) != None,
            "ecl: ",passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            "pid: ",re.match('\d{9}', passport['pid']) != None and len(passport['pid']) == 9,passport)
            
        if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and \
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and \
            int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and \
            ((passport['hgt'][len(passport['hgt']) - 2:] == 'cm' and int(passport['hgt'][:len(passport['hgt']) -2]) >= 150 and int(passport['hgt'][:len(passport['hgt']) -2]) <= 193) or \
            (passport['hgt'][len(passport['hgt']) - 2:] == 'in' and int(passport['hgt'][:len(passport['hgt']) -2]) >= 59 and int(passport['hgt'][:len(passport['hgt']) -2]) <= 76)) and \
            re.match('#[0-9a-f]{6}',passport['hcl']) != None and len(passport['hcl']) == 7 and \
            passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
            re.match('\d{9}', passport['pid']) != None:
            return True
        else:
            return False
    else:
        return False

valid_passports = 0
with open('input.txt', 'r') as f:
    passport = dict()
    for line in f:
        #print("----", line)
        if line.strip() == '':
            #print(passport)
            if passport_validity(passport):
                valid_passports = valid_passports + 1
            passport = dict()
        else:
            tmpPassport = passport
            passport = dict()
            for d in (tmpPassport, get_keyValues(line)):
                passport.update(d)
        
    if passport_validity(passport):
                valid_passports = valid_passports + 1
        
print(valid_passports)