# Based on https://www.youtube.com/watch?v=9UOMZSL0JTg

#file = "puzzle-test.txt"
file = "puzzle-input.txt"

from collections import deque

grid = open(file).read().splitlines()

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

# assertions for part2
assert len(grid) == len(grid[0]) # grid is a square 
size = len(grid)
steps = 26501365
assert sr == sc == size // 2 # starting point in the middle
assert steps % size == size // 2 # back to the middle point

def fill(sr, sc, ss):
    ans = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, ss)])

    while q:
        r, c, s = q.popleft()

        #alternating -> the second steps is the answer
        if s % 2 == 0:
            ans.add((r, c))
        if s == 0:
            continue
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nr >= len(grid) or nc >= len(grid[0]) or nc < 0 or grid[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            q.append((nr, nc, s - 1))
    return len(ans)

##########################
#  part 1: 3733
##########################
print(fill(sr, sc, 64)) 

##########################
#  part 2: 617729401414635
##########################
grid_width = steps // size - 1
odd = (grid_width // 2 * 2 + 1) ** 2 # round down
even = ((grid_width + 1) // 2 * 2) ** 2  # round up

# -------------------------------#
#### Case: fully filled grids ####
# -------------------------------#
odd_points = fill(sr, sc, size * 2 + 1) # number of steps for all "odd" grids
even_points = fill(sr, sc, size * 2) # number of steps for all "even" grids

# -------------------------------#
####      Case: corners       ####
# -------------------------------#
corner_t = fill(size - 1, sc, size - 1) # size - 1 just enough to get to the top row
corner_r = fill(sr, 0, size - 1) # size - 1 just enough to get to the top row
corner_b = fill(0, sc, size - 1) # size - 1 just enough to get to the top row
corner_l = fill(sr, size - 1, size - 1) # size - 1 just enough to get to the top row

# -------------------------------#
# Case: small segments at sides  #
# -------------------------------#
small_tr = fill(size - 1, 0, size // 2 - 1) # smaller segments (calculation see video)
small_br = fill(0, 0, size // 2 - 1) # smaller segments (calculation see video)
small_tl = fill(size - 1, size - 1, size // 2 - 1) # smaller segments (calculation see video)
small_bl = fill(0, size - 1, size // 2 - 1) # smaller segments (calculation see video)

# -------------------------------#
# Case: larger segments at sides #
# -------------------------------#
large_tr = fill(size - 1, 0, size * 3 // 2 - 1) # smaller segments (calculation see video)
large_br = fill(0, 0, size * 3 // 2 - 1) # smaller segments (calculation see video)
large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1) # smaller segments (calculation see video)
large_bl = fill(0, size - 1, size * 3 // 2 - 1) # smaller segments (calculation see video)

sum = (odd * odd_points) + (even * even_points) + corner_t + corner_b + corner_l + corner_r + (grid_width + 1) * (small_bl + small_br + small_tl + small_tr) + grid_width * (large_bl + large_br + large_tl + large_tr)

print(sum)


