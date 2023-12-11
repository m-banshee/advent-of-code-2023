# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())

import numpy as np

content = []
for line in open("input.txt"):
   content.append(line.strip())

directions = content.pop(0)
content.pop(0)

for i, row in enumerate(content):
   content[i] = row.split(" = ")

def returnRow(dest):
    for r in content:
        if dest in r[0]:
            return r

node = returnRow('AAA')
count = 0
while node[0] != 'ZZZ':
    dir = directions[count % len(directions)]
    if dir == 'R':
        node = returnRow(node[1][-4:-1])
    elif dir == 'L':
        node = returnRow(node[1][1:4])
    
    count += 1

answer = count

print("Part 1: " + str(answer))
        
nodeStarts = []
countLists = [0, 0, 0, 0, 0, 0]

for n in content:
    if n[0][-1] == 'A':
        nodeStarts.append(n)

for i, c in enumerate(countLists):
    count = 0
    node = nodeStarts[i]
    while node[0][-1] != 'Z':
        # print(count)
        dir = directions[count % len(directions)]
        if dir == 'R':
            node = returnRow(node[1][-4:-1])
        elif dir == 'L':
            node = returnRow(node[1][1:4])

        count += 1

    countLists[i] = count
print(countLists)
val = int(np.lcm.reduce(countLists))
print(val)
print("Part 2: " + str(int(np.lcm.reduce(countLists, dtype='int64'))))