boardinggroups = []

currentBoardinggroup = []
totalSum = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            boardinggroups.append(currentBoardinggroup)
            totalSum = totalSum + len(currentBoardinggroup)
            currentBoardinggroup = []
        else:
            for char in line.strip():
                if char not in currentBoardinggroup:
                    currentBoardinggroup.append(char)
boardinggroups.append(currentBoardinggroup)
totalSum = totalSum + len(currentBoardinggroup)
print(totalSum)