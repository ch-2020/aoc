import numpy as np
import re

def calc_diff(a):
    if all(x == 0 for x in a): 
        return (a, 0)
    else:
        last_value = a[-1]
        arr = np.diff(a)
        new_arr, diff = calc_diff(arr)
        extra_value = last_value + diff 
        return new_arr, extra_value

puzzles = []
with open("puzzle-day-9-input.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        puz = [int(x) for x in re.findall('[+-]?\d+', l)]
        puzzles.append(puz)

sum = 0
for p in puzzles:
    v = calc_diff(p)[1]
    sum = sum + v
print(f'part1: {sum}')

sumb = 0
for p in puzzles:
    p.reverse()
    w = calc_diff(p)[1]
    sumb = sumb + w
print(f'part2: {sumb}')

