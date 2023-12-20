#based on https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day16p2.py
from collections import deque

testfile = "puzzle-test.txt"
inputfile = "puzzle-16-input.txt"
currentfile = inputfile

with open(currentfile, "r") as f:
    input = f.read().splitlines()
    
def get_steps_num(r, c, dr, dc):
    # row, column, dir row, dir column
    a = [(r, c, dr, dc)]
    seen = set() 
    q = deque(a)

    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc

        if r < 0 or r >= len(input) or c < 0 or c >= len(input[0]):
            continue

        ch = input[r][c]
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:                    
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
    
    coords = {(r, c) for (r, c, _, _) in seen}
    return len(coords)

#part1
p1_max_val_res = get_steps_num(0, -1, 0, 1)
print(p1_max_val_res)

#part2
max_val = 0
for i in range(0, len(input[0])):
    max_val = max(max_val, get_steps_num(-1, i, 1, 0))
    max_val = max(max_val, get_steps_num(len(input), i, -1, 0))

for j in range(0, len(input)):
    max_val = max(max_val, get_steps_num(j, -1, 0, 1))
    max_val = max(max_val, get_steps_num(j, len(input[0]), 0, -1))

print(max_val)
