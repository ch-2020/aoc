from global_ import globalvariables as gv
f = gv.filecontent
steps = f.split("\n")

commands = []
for s in steps:
    dir, cnt = s.split(" ")
    commands.append((dir, int(cnt)))

move = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1),
    "diagUR": (1, 1),
    "diagDR": (1, -1),
    "diagUL": (-1, 1),
    "diagDL": (-1, -1)
}
direc = {
    (1, 0): "R",
    (0, 1): "U",
    (-1, 0): "L",
    (0, -1): "D",
    (1, 1): "diagUR",
    (1, -1): "diagDR",
    (-1, 1): "diagUL",
    (-1, -1): "diagDL"
}

prevB = [[0,0]]*10
currB = [[0,0]]*10
headpath = []
stepped = set()

for dir, cnt in commands:
    for c in range(cnt):
        prevB = currB.copy()
        currB[0] = [currB[0][0] + move[dir][0], currB[0][1] + move[dir][1]]

        for i in range(0, len(currB) - 1):
            xf, yf = currB[i]
            xe, ye = currB[i+1]

            # not touching
            if abs(xf - xe) > 1 or abs(yf - ye) > 1:
                # diagonal
                if xf != xe and yf != ye:
                    currB[i+1] = [int(xe + (xf-xe)/abs(xf-xe)), int(ye + (yf-ye)/abs(yf-ye))]
                elif xf == xe:
                    currB[i+1] = [xe, int(ye + (yf-ye)/abs(yf-ye))]
                elif yf == ye:
                    currB[i+1] = [int(xe + (xf-xe)/abs(xf-xe)), ye]
            
        stepped.add((currB[-1][0], currB[-1][1]))
        headpath.append((currB[0][0], currB[0][1]))


from library.coord_visu import DrawCoordMap

mapt = DrawCoordMap(stepped)
mapt.draw_map(200)
maph = DrawCoordMap(headpath)
maph.draw_map(200)

print(f"len: {len(stepped)}")