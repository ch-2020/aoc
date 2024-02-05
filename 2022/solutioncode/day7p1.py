from global_ import globalvariables as gv
f = gv.filecontent

import pprint as pp 

dirlist = {"/": []}
dircontent = {"/": []}
prevdir = []
currendir = ""

for l in f.split("\n"):
    if l[0] == "$":
        sym, *cmd = l.split()
        if cmd[0] == "cd" and cmd[1] != "..":
            prevdir.append(currendir)
            currendir = cmd[1]

        elif cmd == "cd" and cmd[1] == "..":
            currendir = prevdir.pop()
        
    else:
        c1, c2 = l.split(" ")
        if c1 == "dir":
            if c2 not in dirlist.keys():
                dirlist[c2] = []
            if c2 not in dircontent.keys():
                dircontent[c2] = []
            dirlist[currendir] += c2
        else:
            dircontent[currendir] += [int(c1)]

def addsum(dirname, inputlist: list):
    total = 0
    if inputlist == []:
        return sum(map(int, dircontent[dirname]))
    else:
        for v, i in enumerate(inputlist):
            if i in dirlist.keys():
                total += addsum(i, dirlist[i])
        total += sum(map(int, dircontent[dirname]))
    return total

res = {}
totalstorage = 0
for k in dirlist.keys():
    size = addsum(k, dirlist[k])
    res[k] = size
    if size <= 100000:
        totalstorage += size

pp.pprint(dirlist)
pp.pprint(res)
print(totalstorage)