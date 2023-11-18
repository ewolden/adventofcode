crates = []
working_on_crates = True
with open('5input.txt','r') as f:
    for line in f:
        if line.rstrip() == '':
            working_on_crates = False
        elif working_on_crates:
            if '[' in line:
                structured = line.replace('[', ' ').replace(']', ' ').replace('   ',',').replace(' ', '').rstrip()
                for idx, letter in enumerate(structured.split(',')):
                    if idx > len(crates)-1:
                        crates.append([])
                    if letter != '':
                        crates[idx].append(letter)
        else:
            structured = line.rstrip().split(' ')
            for move in range(int(structured[1])):
                crates[int(structured[5])-1].insert(move,crates[int(structured[3])-1].pop(0))
key = ''
for crate in crates:
    if len(crate) > 0:
        key = key + crate[0]
print(key)