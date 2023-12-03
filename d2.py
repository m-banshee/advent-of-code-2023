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
   games.append(line.strip().split(': ')[1].split('; '))

maxes = [13, 12, 14]

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
                if int(t.split(' ')[0]) > maxes[0]:
                    okayGame = False
                    break
            if 'red' in t:
                if int(t.split(' ')[0]) > maxes[1]:
                    okayGame = False
                    break
            if 'blue' in t:
                if int(t.split(' ')[0]) > maxes[2]:
                    okayGame = False
                    break
            
    if okayGame:
        sum += gameCount

print("Part 1: " + str(sum))

sum = 0
for g in games:
    maxes = [0, 0, 0]
    for s in g:
        temp = s.split(', ')
        for t in temp:
            if 'green' in t:
                if int(t.split(' ')[0]) > maxes[0]:
                    maxes[0] = int(t.split(' ')[0])
            if 'red' in t:
                if int(t.split(' ')[0]) > maxes[1]:
                    maxes[1] = int(t.split(' ')[0])
            if 'blue' in t:
                if int(t.split(' ')[0]) > maxes[2]:
                    maxes[2] = int(t.split(' ')[0])
            
    sum += maxes[0]*maxes[1]*maxes[2]

print("Part 2: " + str(sum))