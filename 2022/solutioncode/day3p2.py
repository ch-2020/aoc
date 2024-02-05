from global_ import globalvariables as gv
f = gv.filecontent

def getord(c):
    if ord(c) >= 97: # lowercase
        return ord(c) - 96
    else: # uppercase
        return ord(c) - 38

def findcommon(listofthree):
    c = set(listofthree[0]) & set(listofthree[1]) & set(listofthree[2])
    if len(c) == 1:
        char = c.pop()
        num = getord(char)
        return num
    return 0

items = f.split("\n")
res = []

sum = 0
for i in range(0, len(items), 3):
    print(items[i:i+3])
    sum += findcommon(items[i:i+3])
print(sum)