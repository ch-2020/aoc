from global_ import globalvariables as gv
f = gv.filecontent
lines = f.split("\n")
rows = len(lines)
cols = len(lines[0])

seen = set()

for c in range(cols):
    seen.add((0, c))
    seen.add((rows - 1, c))

for r in range(1, rows):
    seen.add((r, 0))
    seen.add((r, cols - 1))

def find_largest_num(s):
    max = (0, int(s[0]))
    res = [max]
    for i, v in enumerate(s):
        if int(v) > max[1]:
            res.append((i, int(v)))
            max = (i, int(v))
    return max, res

for r in range(1, rows-1):
    m, res = find_largest_num(lines[r][:-1])
    for i in res:
        seen.add((r, i[0]))

    rev = lines[r][::-1]
    m, res = find_largest_num(rev[:-1])
    for i in res:
        seen.add((r, cols - 1 - i[0]))

otherdir = ["".join(ele) for ele in zip(*lines)]

for c in range(1, cols - 1):
    m, res = find_largest_num(otherdir[c][:-1])
    for i in res:
        seen.add((i[0], c))
    
    rev = otherdir[c][::-1]
    m, res = find_largest_num(rev[:-1])
    for i in res:
        seen.add((rows - 1 - i[0], c))

print(sorted(seen))
print(len(seen))