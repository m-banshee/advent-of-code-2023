# Get lines
content = []
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
# content = list(open('input.txt', 'r').read())

times = []
distances = []
f = open('input.txt', 'r')
times = f.readline().split()
times.pop(0)
distances = f.readline().split()
distances.pop(0)

answer = 1

for i, t in enumerate(times):
    timeMs = int(times[i])
    distMm = int(distances[i])
    
    ans = 0

    if timeMs % 2:
        midway1 = (timeMs - 1) / 2
        midway2 = (timeMs + 1) / 2
    else:
        midway1 = (timeMs) / 2
        midway2 = (timeMs) / 2
        ans -= 1

    
    while True:
        result = midway1 * midway2
        if result <= distMm:
            break
        else:
            midway1 -= 1
            midway2 += 1
            ans += 2
    
    answer *= ans

print(answer)

print("Part 1: " + str(answer))

bigTime = ""
for i in times:
    bigTime += i

bigDist = ""
for i in distances:
    bigDist += i

answer = 1
ans = 0
timeMs = int(bigTime)
distMm = int(bigDist)

if timeMs % 2:
    midway1 = (timeMs - 1) / 2
    midway2 = (timeMs + 1) / 2
else:
    midway1 = (timeMs) / 2
    midway2 = (timeMs) / 2
    ans -= 1

    
while True:
    result = midway1 * midway2
    if result <= distMm:
        break
    else:
        midway1 -= 1
        midway2 += 1
        ans += 2
    
answer *= ans

print("Part 2: " + str(answer))