#------------------------------------------------
# Part 2
#------------------------------------------------
from collections import deque
#use array instead of tuple to manipulate easier
bricks = [list(map(int, line.replace("~", ",").split(",")))for line in open("puzzle-input.txt")]
bricks.sort(key=lambda brick: brick[2])

def overlaps(a, b):
    # if max of starting points is less than min of ending points
    # do this for both x and y coordinates
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for index, brick in enumerate(bricks):
    max_z = 1
    for check in bricks[:index]:
        if overlaps(brick, check):
            # determine the max z where the brick will lands (for all bricks below it)
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

bricks.sort(key=lambda brick: brick[2])

k_supports_v = {i: set() for i in range(len(bricks))}
v_supports_k = {i: set() for i in range(len(bricks))}

# generate supporting bricks
for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0
for i in range(len(bricks)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q: 
        j = q.popleft()
        for k in k_supports_v[j] - falling: # set substraction, w/o considering those already felt
            if v_supports_k[k] <= falling: # subset of falling
                q.append(k)
                falling.add(k)
    # because we added i at first in the falling
    print(falling)
    total += len(falling) - 1

print(total) #part2: 68525
