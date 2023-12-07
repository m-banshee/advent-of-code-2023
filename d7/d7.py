# Get lines
#for line in open("input.txt"):
#    line = line.strip()

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())

def swap(a,b):
   a, b, c = c, a, b

content = []
for line in open("input.txt"):
   content.append(line.strip().split())

def countCards(string):
   return {x:string.count(x) for x in string}

highCard = []
onePair = []
twoPair = []
threeOfaKind = []
fullHouse = []
fourOfaKind = []
fiveOfaKind = []

for row in content:
    temp = countCards(row[0])
    # temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    temp = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))
    if len(temp) == 5:
        highCard.append(row)
    elif len(temp) == 4:
        onePair.append(row)
    elif len(temp) == 3:
        keyVal = list(temp.items())[0:2]
        if keyVal[0][1] == 2 and keyVal[1][1] == 2:
            twoPair.append(row)
        else:
            threeOfaKind.append(row)
    elif len(temp) == 2:
        # keyVal = list(temp.keys())[0]
        keyVal = list(temp.items())[0:2]
        if keyVal[0][1] == 3 and keyVal[1][1] == 2:
            fullHouse.append(row)
        else:
            fourOfaKind.append(row)
    else:
        fiveOfaKind.append(row)

def translateCard(ch):
    val = 0
    if ch == "T":
        val = 10
    elif ch == "J":
        val = 11
    elif ch == "Q":
        val = 12
    elif ch == "K":
        val = 13
    elif ch == "A":
        val = 14
    else:
        val = int(ch)
    
    return val

def swapTwoHands(h1, h2):
    for card in range(0, 5):
        v1 = translateCard(h1[card])
        v2 = translateCard(h2[card])
        if v1 > v2:
            return True
        if v1 < v2:
            return False
    
    return False

def sortHands(hands):
    swap = True
    while swap:
        swap = False
        for row in range(0, len(hands)-1):            
            if swapTwoHands(hands[row][0], hands[row+1][0]):
                hands[row], hands[row+1] = hands[row+1], hands[row]
                swap = True

        # if original == hands:
        #     break
      
sortHands(highCard)
sortHands(onePair)
sortHands(twoPair)
sortHands(threeOfaKind)
sortHands(fullHouse)
sortHands(fourOfaKind)
sortHands(fiveOfaKind)

answer = 0
position = 1
for n in highCard:
    answer += int(n[1])*position
    position += 1
for n in onePair:
    answer += int(n[1])*position
    print(int(n[1])*position)
    position += 1
for n in twoPair:
    answer += int(n[1])*position
    position += 1
for n in threeOfaKind:
    answer += int(n[1])*position
    position += 1
for n in fullHouse:
    answer += int(n[1])*position
    position += 1
for n in fourOfaKind:
    answer += int(n[1])*position
    position += 1
for n in fiveOfaKind:
    answer += int(n[1])*position
    position += 1

print("Part 1: " + str(answer))

answer = 0
sum = 0

print("Part 2: " + str(answer))