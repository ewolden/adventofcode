import re
validnum = 0
invalidnum = 0
debug = False
with open('input.txt', 'r') as f:
	for line in f:
		letter = line.split(':')[0].split(' ')[1].strip()
		number1 = int(line.split(':')[0].split('-')[0]) - 1
		number2 = int(line.split(':')[0].split(' ')[0].split('-')[1]) - 1
		string = line.split(':')[1].strip()
		if debug:
			print("letter: ",letter, " number1: ",number1, " number2: ", number2, " string: ", string)
		if (string[number1] == letter) ^ (string[number2] == letter):
		#len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) >= int(line.split(':')[0].split('-')[0]) and len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) <= int(line.split(':')[0].split(' ')[0].split('-')[1]):
			validnum = validnum + 1
		else:
			invalidnum = invalidnum + 1
print("valid: ", validnum, " invalid: ",invalidnum)
