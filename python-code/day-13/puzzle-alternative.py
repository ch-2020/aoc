def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1] #flip the upper part
        below = grid[r:]

        above = above[:len(below)] #slice to the smaller part
        below = below[:len(above)]

        if above == below:
            return r
    return 0

def find_mirror_part2(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1] #flip the upper part
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x,y)) for x, y in zip(above, below)) == 1:
            return r
    return 0
    
total = 0
total_part2 = 0
for block in open("puzzle-day-13-input.txt").read().split("\n\n"):
    grid = block.splitlines()
    
    # PART1
    row = find_mirror(grid)
    total += row * 100 # horizontal will multiply by 100

    col = find_mirror(list(zip(*grid))) # expand and transpose
    total += col

    # PART2
    row2 = find_mirror_part2(grid)
    total_part2 += row2 * 100 # horizontal will multiply by 100

    col2 = find_mirror_part2(list(zip(*grid))) # expand and transpose
    total_part2 += col2

print(total)
print(total_part2)
