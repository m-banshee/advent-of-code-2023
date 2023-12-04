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
   content.append(line.strip().split(" | "))

winners = []
picks = []
for ch in content:
   winners.append(ch[0].split(": ")[1].split(" "))
   picks.append(ch[1].split(" "))

answer = 0
for row, p in enumerate(picks):
    score = 0
    for n in p:
        if n in winners[row] and n != "":
            if score == 0:
                score = 1
            else: 
                score *= 2
    
    answer += score
   
print("Part 1: " + str(answer))

numCards = []

for w in winners:
    numCards.append(0)

for row, p in enumerate(picks):
    score = 0
    for n in p:
        if n in winners[row] and n != "":
            score += 1
    
    for i in range(1, score+1):
        if row + i < len(numCards):
            numCards[row + i] += numCards[row]+1

print("Part 2: " + str(sum(numCards) + len(numCards)))