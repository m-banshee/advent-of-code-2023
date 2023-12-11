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
   temp = line.strip().split()
   tempList = []
   for t in temp:
      tempList.append(int(t))
   content.append(tempList)

manyRows = []
tempList = []
answer = 0

for row in content:
    tempList = row.copy()
    manyRows = []
    manyRows.append(tempList)
    while True:
        tempList = []
        for i in range(0, len(manyRows[-1]) - 1):
            tempList.append(manyRows[-1][i + 1] - manyRows[-1][i])
        
        manyRows.append(tempList)

        if not any(tempList):
            break
                
    
    manyRows[-1].append(0)
    for n, row in enumerate(manyRows):
        if n == len(manyRows) - 1:
            break
        manyRows[-2 - n].append(manyRows[-1 - n][-1] + manyRows[-2 - n][-1])

    answer += manyRows[0][-1]

print("Part 1: " + str(answer))

manyRows = []
tempList = []
answer = 0

for row in content:
    tempList = row.copy()
    manyRows = []
    manyRows.append(tempList)
    while True:
        tempList = []
        for i in range(0, len(manyRows[-1]) - 1):
            tempList.append(manyRows[-1][i + 1] - manyRows[-1][i])
        
        manyRows.append(tempList)

        if not any(tempList):
            break
                
    for n in manyRows:
        n.reverse()
    
    manyRows[-1].append(0)
    for n, row in enumerate(manyRows):
        if n == len(manyRows) - 1:
            break
        manyRows[-2 - n].append(manyRows[-2 - n][-1] - manyRows[-1 - n][-1])

    answer += manyRows[0][-1]

print("Part 2: " + str(answer))