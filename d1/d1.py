# Get lines
content = []
for line in open("input.txt"):
   line = line.strip()
   content.append(line)

# f = open('input.txt', 'r')
# content = f.readlines()
# content = f.read().splitlines()

# Get character list
#content = list(open('input.txt', 'r').read())

# Part 1
sum = 0
for l in content:
    num1 = 0
    num2 = 0
    for i in l:
      if i.isdigit():
        num1 = i
        break
    for count in range(len(l)-1,0,-1):
        if l[count].isdigit():
            num2 = l[count]
            break
    if num2 == 0:
       num2 = num1
    sum += int(num1 + num2)

print("Part 1: " + str(sum))

numArray = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def findNum(input, i):
    if input[i].isdigit():
        return input[i]
    
    for j, n in enumerate(numArray):
        if n in input[i:i+len(numArray[j])]:
            return str(j)
            
    return None

sum = 0
for l in content:
    num1 = 0
    num2 = 0

    for count in range(0,len(l),1):
        num1 = findNum(l, count)
        if num1:
           break

    for count in range(len(l)-1,0,-1):
        num2 = findNum(l, count)
        if num2:
           break 
    
    if num2 == None:
       num2 = num1

    sum += int(num1 + num2)

print("Part 2: " + str(sum))
