from global_ import globalvariables as gv
f = gv.filecontent

import re

col1 = []
col2 = []

for l in f.split("\n"):
    num1, num2 = re.findall(r'\d+', l)
    col1.append(int(num1))
    col2.append(int(num2))

# calculate recurring times in right column and store in dict
rightcount = dict()
for nr, itemr in enumerate(col2):
    if rightcount.get(itemr) == None:
        rightcount[itemr] = 1
    else:
        rightcount[itemr] += 1

# sum up
apprtimes = 0
sum = 0
for nl, iteml in enumerate(col1):
    if rightcount.get(iteml) == None:
        apprtimes = 0
    else:
        apprtimes = rightcount[iteml]
    sum += iteml * apprtimes

print(sum)