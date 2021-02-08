import random

numBranches = 3

numRouters = 20

branchesList = []

print(branchesList)

for i in range(numRouters):
    bufferList = []

    numRange = list(range(1,21))
    print(i+1)
    numRange.remove(i+1)
    random.shuffle(numRange)

    for j in range(numBranches):
            bufferList.append(numRange.pop())
    branchesList.append(bufferList)

print(branchesList)

fp = open("networkTop.txt",'w')

for i in range(len(branchesList)):
    fp.write(str(i+1) + ':')
    for j in range(len(branchesList[i])):
        if j != 0:
            fp.write(',')
        fp.write(str(branchesList[i][j]))
    fp.write('\n')
fp.close()
