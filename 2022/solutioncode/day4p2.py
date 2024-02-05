from global_ import globalvariables as gv
f = gv.filecontent

sum = 0
for l in f.split("\n"):
    both = l.split(",")
    r1f, r1e = map(int, both[0].split("-"))
    r2f, r2e = map(int, both[1].split("-"))
    if (r1f >= r2f and r1f <= r2e) or (r2f >= r1f and r2f <= r1e):
        sum += 1

print(sum)