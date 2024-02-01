from global_ import globalvariables as gv
f = gv.filecontent

blocks = f.split("\n\n")

cals = []
for b in blocks:
    cal = sum(map(int, list(x for x in b.split("\n"))))
    cals.append(cal)

scals = sorted(cals, reverse=True)
total = sum(scals[0:3])
print(total)