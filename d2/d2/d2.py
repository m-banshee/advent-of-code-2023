# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())
games = []
for line in open("input.txt"):
   line = line.strip().split(': ')
   games.append(line[1].split('; '))

maxRed = 12
maxGreen = 13
maxBlue = 14

sum = 0
gameCount = 0
okayGame = True
for g in games:
    okayGame = True
    gameCount += 1
    for s in g:
        temp = s.split(', ')
        for t in temp:
            if 'green' in t:
                if int(t.split(' ')[0]) > maxGreen:
                    okayGame = False
                    break
            if 'red' in t:
                if int(t.split(' ')[0]) > maxRed:
                    okayGame = False
                    break
            if 'blue' in t:
                if int(t.split(' ')[0]) > maxBlue:
                    okayGame = False
                    break
            
    if okayGame:
        sum += gameCount

print("Part 1: " + str(sum))

maxRed = 0
maxGreen = 0
maxBlue = 0
sum = 0
for g in games:
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for s in g:
        temp = s.split(', ')
        for t in temp:
            if 'green' in t:
                if int(t.split(' ')[0]) > maxGreen:
                    maxGreen = int(t.split(' ')[0])
            if 'red' in t:
                if int(t.split(' ')[0]) > maxRed:
                    maxRed = int(t.split(' ')[0])
            if 'blue' in t:
                if int(t.split(' ')[0]) > maxBlue:
                    maxBlue = int(t.split(' ')[0])
            
    sum += maxGreen*maxRed*maxBlue

print("Part 2: " + str(sum))