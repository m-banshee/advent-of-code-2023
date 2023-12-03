# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
# content = list(open('input.txt', 'r').read())
content = []
for line in open("input.txt"):
   content.append(line.strip())

def getNum(y,x):
    rightIndex = x
    leftIndex = x - 1

    while rightIndex < len(content[y]) and content[y][rightIndex].isdigit():
        if str(y) + ", " + str(rightIndex) in foundDict:
            return 0
        else:
            foundDict[str(y) + ", " + str(rightIndex)] = True
            rightIndex += 1

    while leftIndex >= 0 and content[y][leftIndex].isdigit():
        if str(y) + ", " + str(leftIndex) in foundDict:
            return 0
        else:
            foundDict[str(y) + ", " + str(leftIndex)] = True
            leftIndex -= 1
    
    return int(content[y][leftIndex+1:rightIndex])

def checkForNumPart1(y, x):
    sum = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if content[y+dy][x+dx].isdigit():
                sum += getNum(y+dy, x+dx)
    
    return sum

def checkForNumPart2(y, x):
    nums = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if content[y+dy][x+dx].isdigit():
                temp = getNum(y+dy, x+dx)
                if temp != 0:
                    nums.append(temp)

    if len(nums) == 2:
        return nums[0]*nums[1]
    else:
        return 0

foundDict = {}
rowCount = 0
answer = 0

for row in content:
    for ch in range(0, len(row)):
        if row[ch] != '.' and not row[ch].isdigit():
            answer += checkForNumPart1(rowCount, ch)
    
    rowCount += 1

print("Part 1: " + str(answer))

foundDict = {}
rowCount = 0
answer = 0

for row in content:
    for ch in range(0, len(row)):
        if row[ch] != '.' and not row[ch].isdigit():
            if row[ch] == '*':
                answer += checkForNumPart2(rowCount, ch)
    rowCount += 1


print("Part 2: " + str(answer))