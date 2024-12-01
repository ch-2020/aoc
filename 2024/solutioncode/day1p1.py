from global_ import globalvariables as gv
f = gv.filecontent

import re

col1 = []
col2 = []

for l in f.split("\n"):
    num1, num2 = re.findall(r'\d+', l)
    col1.append(int(num1))
    col2.append(int(num2))

col1.sort()
col2.sort()

sum = 0
for n, item in enumerate(col1):
    sum += abs(col1[n] - col2[n])

print(sum)