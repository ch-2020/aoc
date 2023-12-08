import numpy as np

instructions = []
maps = {}
with open("puzzle-day-8-input.txt", "r") as f:
    instructions = np.array([*f.readline().strip()])
    hits = np.where(instructions == 'R')
    instructions = np.zeros(len(instructions), dtype=int)
    instructions[hits] = 1
    f.readline()
    for line in f:
        l = line.strip().replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
        maps[l[0]] = l[1:]

def solve(cur = 'AAA', end_func = lambda c: c == 'ZZZ'):
    for i in range(1000000):
        ins = instructions[i % instructions.size]
        cur = maps[cur][ins]
        if end_func(cur):
            break
    return (i+1, cur)

print(f"Part 1: {solve()[0]}")

curs = [c for c in maps.keys() if c[2] == 'A']
metadata = []
for cur in curs:
    res, _ = solve(cur, lambda c: c[2] == 'Z')
    metadata.append(res)
    print(metadata)
result = np.lcm.reduce(np.array(metadata, dtype=np.int64))
print(f"Part 2: {result}")