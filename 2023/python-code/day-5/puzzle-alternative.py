# Alternative online for part1
# https://www.youtube.com/watch?v=NmxHw_bHhGM

import os

filepath = os.path.join(os.path.dirname(__file__), 'puzzle-test.txt')
seeds, *blocks = open(filepath).read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new

print(min(seeds))
