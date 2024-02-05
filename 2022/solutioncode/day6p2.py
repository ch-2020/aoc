from global_ import globalvariables as gv
f = gv.filecontent

def issimilar(str):
    for s in list(str):
        if int(str.count(s)) > 1:
            return True
    return False

for c in range(0, len(f)):
    sim = issimilar(f[c:c+14])
    if sim == False:
        print(c+14)
        break
