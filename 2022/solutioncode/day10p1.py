from global_ import globalvariables as gv
f = gv.filecontent
steps = f.split("\n")

X = 1
cycle = 1
res = []

def checkcycle(cyc, num):
    if cyc in [20, 60, 100, 140, 180, 220]:
        res.append(cyc * num)

for s in steps:
    if s[0] == "a": #addx
        cmd, num = s.split(" ")
        cycle += 1
        checkcycle(cycle, X)
        cycle += 1
        X += int(num)
        checkcycle(cycle, X)

    else: #noop
        cycle += 1
        checkcycle(cycle, X)

print(res)
print(sum(res))