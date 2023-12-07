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
   content.append([line.strip().split()[0],line.strip().split()[1], ""])

def countCards(string):
   return {x:string.count(x) for x in string}

highCard = []
onePair = []
twoPair = []
threeOfaKind = []
fullHouse = []
fourOfaKind = []
fiveOfaKind = []
handTypes = [highCard, onePair, twoPair, threeOfaKind, fullHouse, fourOfaKind, fiveOfaKind]

def scrubWilds(sortedCards, oldHand):
    if 'J' in temp:
        if list(sortedCards.keys())[0] == 'J' and len(sortedCards) > 1:
            return oldHand.replace('J', list(sortedCards.keys())[1])
        else:
            return oldHand.replace('J', list(sortedCards.keys())[0])
    else:
        return oldHand

for row in content:
    temp = countCards(row[0])
    temp = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))

    row[2] = scrubWilds(temp, row[0])
    temp = countCards(row[2])
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
        keyVal = list(temp.items())[0:2]
        if keyVal[0][1] == 3 and keyVal[1][1] == 2:
            fullHouse.append(row)
        else:
            fourOfaKind.append(row)
    else:
        fiveOfaKind.append(row)

def translateCard(ch):
    if ch == "T":
        return 10
    elif ch == "J":
        return 1
    elif ch == "Q":
        return 12
    elif ch == "K":
        return 13
    elif ch == "A":
        return 14
    else:
        return int(ch)

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

for n in handTypes:
    sortHands(n)

answer = 0
position = 1
for t in handTypes:
    for n in t:
        answer += int(n[1])*position
        position += 1

print("Part 2: " + str(answer))