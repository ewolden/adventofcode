import re
validnum = 0
invalidnum = 0
debug = True
with open('input.txt', 'r') as f:
	for line in f:
		if debug:
			print(line.split(':')[0].split(' ')[1].strip()
					+'{'
					+line.split(':')[0].split('-')[0]
					+','
					+line.split(':')[0].split(' ')[0].split('-')[1]
					+'}')
			print(line.split(':')[1].strip())
			print(len(re.findall(
					line.split(':')[0].split(' ')[1].strip()
					,line.split(':')[1])))

			#print(len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) >= line.split(':')[0].split('-')[0] and len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) <= line.split(':')[0].split(' ')[0].split('-')[1]

		if len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) >= int(line.split(':')[0].split('-')[0]) and len(re.findall(line.split(':')[0].split(' ')[1].strip(),line.split(':')[1])) <= int(line.split(':')[0].split(' ')[0].split('-')[1]):
			validnum = validnum + 1
		else:
			invalidnum = invalidnum + 1
print(validnum)
print(invalidnum)