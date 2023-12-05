# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())
import queue

content = list(open('input.txt', 'r').read().split("\n\n"))
seeds = [int(i) for i in content[0].split("seeds: ")[1].split()]
seedSoil = [i for i in content[1].split(" map:\n")[1].split("\n")]
soilFert = [i for i in content[2].split(" map:\n")[1].split("\n")]
fertWater = [i for i in content[3].split(" map:\n")[1].split("\n")]
waterLight = [i for i in content[4].split(" map:\n")[1].split("\n")]
lightTemp = [i for i in content[5].split(" map:\n")[1].split("\n")]
tempHum = [i for i in content[6].split(" map:\n")[1].split("\n")]
humLocation = [i for i in content[7].split(" map:\n")[1].split("\n")]
locations = {}

def convert(lookup, s):
    for row in lookup:
        dest = int(row.split()[0])
        src = int(row.split()[1])
        range = int(row.split()[2])
        newS = s

        if s >= src and s <= src + range:
            newS += dest - src
            break
    return newS

def convert2(lookup, startSpan):
    newS = []
    tempQ = queue.Queue()
    for start_span in startSpan:
        for n in start_span:
            tempQ.put(n)

    while tempQ.qsize() > 0:
        start_span = tempQ.get()
        start = start_span[0]
        span = start_span[1]
        ognum = start_span[2]

        if span == 0:
            continue

        found = False
        for row in lookup:
            dest = int(row.split()[0])
            src = int(row.split()[1])
            range = int(row.split()[2])

            if start >= src and start < (src + range) and (start + span) >= (src + range):
                diff = dest - src
                tempQ.put([(src + range), span - ((src + range) - start), ognum + span - ((src + range) - start)])
                newS.append([diff + start, (src + range) - start, ognum])
                found = True
            elif start <= src and (start + span) > src and (start + span) < (src + range):
                diff = dest - src
                tempQ.put([start, src - start, ognum])
                newS.append([diff + src, span - (src - start), ognum + (src - start)])
                found = True
            elif start >= src and (start + span) < (src + range):
                newS.append([start + dest - src, span, ognum])
                found = True

        if not found:  
            newS.append([start, span, ognum])
            
    return [newS]

answer = []
for s in seeds:
    soil = convert(seedSoil, s)
    fert = convert(soilFert, soil)
    water = convert(fertWater, fert)
    light = convert(waterLight, water)
    temp = convert(lightTemp, light)
    hum = convert(tempHum, temp)
    location = convert(humLocation, hum)
    answer.append(location)

answer = min(answer)
print("Part 1: " + str(answer))

bigList = []
for s in range(0, len(seeds), 2):
    num = seeds[s]
    span = seeds[s+1]
    bigList.append([num, span, num])

answer = []
import queue
q = queue.Queue()

for s in bigList:
    q.put(s)

answer = -1

while q.qsize() > 0:
    val = q.get()
    soil = convert2(seedSoil, [[val]])
    fert = convert2(soilFert, soil)
    water = convert2(fertWater, fert)
    light = convert2(waterLight, water)
    temp = convert2(lightTemp, light)
    hum = convert2(tempHum, temp)
    location = convert2(humLocation, hum)

    for i in location:
        for n in i:
            if answer == -1:
                answer = n[0]
            elif n[0] < answer:
                answer = n[0]

print("Part 2: " + str(answer))