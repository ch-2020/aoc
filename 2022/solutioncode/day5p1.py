from global_ import globalvariables as gv
f = gv.filecontent

stacksb, stepsb = f.split("\n\n")
stacks = stacksb.split("\n")[::-1]
snum = [int(x) for x in stacks[0].split() if x.isdigit()]
total = snum[-1]

stackitems = [[] for x in range(total)]

for h in stacks[1:]:
    items = h.split("[")
    if len(items) == total + 1:
        for i in range(0, total):
            stackitems[i].append(items[i+1].split("]")[0])
    else:
        for c in range(0, len(h), 4):
            if h[c+1] != " ":
                stackitems[c // 4].append(h[c+1])

commands = []
for s in stepsb.split("\n"):
   commands.append([int(x) for x in s.split() if x.isdigit()])

for c in commands:
    num, fr, to = c
    extract = stackitems[fr-1][-num:][::-1]
    del stackitems[fr-1][-num:]
    stackitems[to-1] = stackitems[to-1] + extract

res = []
for st in stackitems:
    res.append(st[-1])
print(res)
