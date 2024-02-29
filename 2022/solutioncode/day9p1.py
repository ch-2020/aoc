from global_ import globalvariables as gv
f = gv.filecontent
steps = f.split("\n")

commands = []
for s in steps:
    dir, cnt = s.split(" ")
    commands.append((dir, int(cnt)))

H = [0,0]
T = [0,0]
stepped = [(0,0)]
move = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1)
}

for dir, cnt in commands:
    for c in range(cnt):
        H[0] += move[dir][0]
        H[1] += move[dir][1]
        
        if abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1:
            T[0] = H[0] - move[dir][0]
            T[1] = H[1] - move[dir][1]
            stepped.append((T[0], T[1]))

print(len(set(stepped)))
        