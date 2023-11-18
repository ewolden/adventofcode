import math

def findHitTrees(treemap, xSteps, ySteps):
    maplength = len(treemap[0])
    notBottom = True
    numTreesHit = 0
    numClearSteps = 0
    currentPosx = 0
    currentPosy = 0
    while notBottom:
        currentRealposx = currentPosx - math.floor(currentPosx / maplength) * maplength
        #print('y: ', currentPosy, 'x: ', currentPosx, ' realx: ', currentRealposx)
        if treemap[currentPosy][currentRealposx] == '#':
            numTreesHit = numTreesHit + 1
        else:
            numClearSteps = numClearSteps + 1
        #print('y: ', currentPosy, 'x: ', currentPosx, ' realx: ', currentRealposx, '\t -- ', treemap[currentPosy][currentRealposx])
        currentPosx = currentPosx + xSteps
        currentPosy = currentPosy + ySteps

        if currentPosy >= len(treemap):
            notBottom = False
    print('Trees hit:', numTreesHit, ' open spaces: ',numClearSteps)
    return numTreesHit
treemap = []

with open('input.txt', 'r') as f:
    for line in f:
        treemap.append(line.strip())
print("Multiply trees hit",findHitTrees(treemap, 1, 1) * findHitTrees(treemap, 3, 1) * findHitTrees(treemap, 5, 1) * findHitTrees(treemap, 7, 1) * findHitTrees(treemap, 1, 2))

