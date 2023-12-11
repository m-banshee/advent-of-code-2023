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
   content.append(line.strip())

emptyRow = []
for y, row in enumerate(content):
    xFound = False
    for x, col in enumerate(row):
        if col == '#':
            xFound = True
            break
    if not xFound:
        emptyRow.append(y)

emptyCol = []
for x in range(0, len(content[0])):
    yFound = False
    for y in range(0, len(content)):
        if content[y][x] == '#':
            yFound = True
            break
    if not yFound:
        emptyCol.append(x)

locations = []
for y, row in enumerate(content):
    for x, col in enumerate(row):
        if col == '#':
            locations.append([int(y), int(x)])

distancesP1 = []
distancesP2 = []
for n1 in locations:
    for n2 in locations:
        manDist = abs(n2[0] - n1[0]) + abs(n2[1] - n1[1])
        if n1 != n2:
            distancesP1.append(manDist)
            distancesP2.append(manDist)
            for i in range(min(n2[0], n1[0]), max(n2[0], n1[0])):
                if i in emptyRow:
                    distancesP1[-1] += 1
                    distancesP2[-1] += 999999
            for j in range(min(n2[1], n1[1]), max(n2[1], n1[1])):
                if j in emptyCol:
                    distancesP1[-1] += 1
                    distancesP2[-1] += 999999

print("Part 1: " + str(int(sum(distancesP1)/2)))
print("Part 2: " + str(int(sum(distancesP2)/2)))