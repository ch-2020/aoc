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

# cont...


print(sorted(seen))
print(len(seen))