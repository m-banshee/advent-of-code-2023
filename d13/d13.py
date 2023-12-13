# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())

content = []
for line in open("input.txt"):
   content.append(line.strip().split("\n\n")[0])

inputs = []
tempGrid = []
for n in content:
    if n != "":
        tempGrid.append(n)
    else:
        inputs.append(tempGrid)
        tempGrid = []

inputs.append(tempGrid)

def offByOne(line1, line2):
    count = 0
    pos = 0
    for i, (a, b) in enumerate(zip(line1, line2)):
        if a != b:
            pos = i

        count += a != b
        if count == 2:
            return None
    
    if count == 0:
        return None
    
    return pos

def convertAnswer(inList):
    answer = 0
    for a in inList:
        if a[0] == 'r':
            answer += 100*a[1]
        else:
            answer += a[1]
    return answer

def transposeGrid(inGrid):
    outGrid = [""] * len(inGrid[0])

    for r, row in enumerate(inGrid):
        for c, col in enumerate(row):
            outGrid[c] += col

    return outGrid

def createAllGrids(inputGrid, outputGrids):
    for r1, row1 in enumerate(inputGrid):
        for r2, row2 in enumerate(inputGrid):
            pos = offByOne(row1, row2)
            if pos != None:
                temp = inputGrid.copy()
                temp[r1] = temp[r2]
                outputGrids.append(temp)

def findMirrors(inGrid, dontCount, rc):
    for r1, row1 in enumerate(inGrid):
        if r1 + 1 < len(inGrid):
            i = 0
            while True:
                n1 = r1 - i
                n2 = r1 + i + 1

                if inGrid[n1] != inGrid[n2]:
                    break
                elif n1 == 0 or n2 == len(inGrid) - 1:
                    val = int(n1 + (n2 - n1 -1)/2 + 1)
                    if dontCount == None:
                        return val
                    elif not (val == dontCount[1] and rc == dontCount[0]): # this check only needed for part 2
                        return val

                if not (n1 == 0 or n2 == len(inGrid) - 1):
                    i += 1
                else:
                    break

answerList = []
for grid in inputs:
    result = findMirrors(grid, None, None)
    if result == None:
        tGrid = transposeGrid(grid)
        result = findMirrors(tGrid, None, None)

        answerList.append(('c', result))
    else:
        answerList.append(('r', result))

print("Part 1: " + str(convertAnswer(answerList)))

answerListPart2 = []

for x, grid in enumerate(inputs):
    newGrids = []
    createAllGrids(grid, newGrids)

    for n in newGrids:
        result = findMirrors(n, answerList[x], 'r')
        if result != None:
            answerListPart2.append(('r', result))
            break

    newGrids = []
    tGrid = transposeGrid(grid)
    createAllGrids(tGrid, newGrids)      

    for n in newGrids:
        result = findMirrors(n, answerList[x], 'c')
        if result != None:
            answerListPart2.append(('c', result))
            break

print("Part 2: " + str(convertAnswer(answerListPart2)))