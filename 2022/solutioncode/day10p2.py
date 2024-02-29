from global_ import globalvariables as gv
f = gv.filecontent
steps = f.split("\n")

X = 1
cycle = 0
res = []

def checkcycle(cyc, num):
    pixel = (cyc % 40) 
    if pixel >= num and pixel <= num + 2:
        res.append("#")
    else:
        res.append(".")

for s in steps:
    if s[0] == "a": #addx
        cmd, num = s.split(" ")
        cycle += 1
        checkcycle(cycle, X)
        cycle += 1
        checkcycle(cycle, X)
        X += int(num)

    else: #noop
        cycle += 1
        checkcycle(cycle, X)

respixel = ""
for i in range(len(res)):
    if i % 40 == 0:
        respixel += "\n"
    respixel += res[i]
print(respixel)      