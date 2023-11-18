boardinggroups = []

currentBoardinggroup = []
totalSum = 0
newline = True
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            boardinggroups.append(currentBoardinggroup)
            totalSum = totalSum + len(currentBoardinggroup)
            currentBoardinggroup = []
            newline = True
        else:
            if newline:
                currentBoardinggroup = set(line.strip())
                newline = False
            else:
                currentBoardinggroup = list(set(currentBoardinggroup) & set(line.strip()))
boardinggroups.append(currentBoardinggroup)
totalSum = totalSum + len(currentBoardinggroup)
print(totalSum)