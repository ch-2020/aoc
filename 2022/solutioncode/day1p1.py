from global_ import globalvariables as gv
f = gv.filecontent

blocks = f.split("\n\n")

maxcal = 0
for b in blocks:
    cal = sum(map(int, list(x for x in b.split("\n"))))
    if cal > maxcal:
        maxcal = cal

print(maxcal)