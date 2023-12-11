# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())

content = []
# content = list(open('input.txt', 'r').read())
for line in open("input.txt"):
   content.append(line.strip())

grid = {}
start = (0,0)
for y, row in enumerate(content):
    for x, ch in enumerate(row):
      if ch == 'S':
         start = (y, x)
         grid[str(y) + ", " + str(x)] = True

down = content[start[0] + 1][start[1]]
up = content[start[0] - 1][start[1]]
left = content[start[0]][start[1] - 1]
right = content[start[0]][start[1] + 1]
if down == '|' or down == 'J' or down == 'L':
    down = True
if left == '-' or left == 'F' or left == 'L':
    left = True
if up == '|' or up == 'F' or up == '7':
    up = True
if right == '-' or right == '7' or right == 'J':
    right = True

if down and left:
    content[start[0]] = content[start[0]].replace('S', '7')
elif down and up:
    content[start[0]] = content[start[0]].replace('S', '|')
elif down and right:
    content[start[0]] = content[start[0]].replace('S', 'F')
elif left and up:
    content[start[0]] = content[start[0]].replace('S', 'J')
elif left and right:
    content[start[0]] = content[start[0]].replace('S', '-')
elif up and right:
    content[start[0]] = content[start[0]].replace('S', 'L')

curPos = None
curDir = 'D'
while curPos != start:
    if curPos == None:
       curPos = start
    
    y = curPos[0]
    x = curPos[1]
    ch = content[y][x]
    if curDir == 'D':
       curPos = (y+1, x)
       grid[str(y+1) + ", " + str(x)] = True
       if content[y+1][x] == 'L':
          curDir = 'R'
       elif content[y+1][x] == 'J':
          curDir = 'L'
    elif curDir == 'U':
       curPos = (y-1, x)
       grid[str(y-1) + ", " + str(x)] = True
       if content[y-1][x] == 'F':
          curDir = 'R'
       elif content[y-1][x] == '7':
          curDir = 'L'
    elif curDir == 'R':
       curPos = (y, x+1)
       grid[str(y) + ", " + str(x+1)] = True
       if content[y][x+1] == 'J':
          curDir = 'U'
       elif content[y][x+1] == '7':
          curDir = 'D'
    elif curDir == 'L':
       curPos = (y, x-1)
       grid[str(y) + ", " + str(x-1)] = True
       if content[y][x-1] == 'L':
          curDir = 'U'
       elif content[y][x-1] == 'F':
          curDir = 'D'
    else:
       print("should never get here")

print("Part 1: " + str(len(grid)/2))

inside = False
inCount = 0

for y, row in enumerate(content):
   for x, ch in enumerate(row):
        if inside and str(y) + ", " + str(x) not in grid:
            inCount += 1
        if str(y) + ", " + str(x) in grid:
            if content[y][x] == '|' or content[y][x] == 'F' or content[y][x] == '7':
                inside = not inside

print("Part 2: " + str(inCount))