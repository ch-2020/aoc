from global_ import globalvariables as gv
f = gv.filecontent

from collections import deque

hmap = f.split("\n")
width = len(hmap[0])
height = len(hmap)
print(f"w: {width}, h:{height}")

S = E = ()
#find start and end points
for hid, h in enumerate(hmap):
    for wid, w in enumerate(h):
        if w == "S":
            S = (hid, wid)
        elif w == "E":
            E = (hid, wid)
        elif S != () and E != ():
            break
print(f"Start: {S}, End: {E}")

newlineE = hmap[E[0]].replace("E", "z")
hmap[E[0]] = newlineE
newlineS = hmap[S[0]].replace("S", "a")
hmap[S[0]] = newlineS

seen = []
steps = deque()
steps.append((S[0], S[1], 0, 0, 0))
visu = [(S[0], S[1])]

while len(steps) > 0:
    step = steps.popleft()

    h, w, cnt, dx, dy = step
    curr_h = h + dx
    curr_w = w + dy

    if (curr_h, curr_w) == E:
        seen.append((curr_h, curr_w, cnt + 1, dx, dy))    
        print(f"reached dest: {cnt}")
        break

    if curr_h >= 0 and curr_h < height and curr_w >= 0 and curr_w < width:
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nex_h = curr_h + dir[0]
            nex_w = curr_w + dir[1]

            if nex_h >= 0 and nex_h < height and nex_w >= 0 and nex_w < width:
                h_nextstep = ord(hmap[nex_h][nex_w])
                h_current = ord(hmap[curr_h][curr_w])
                count = cnt + 1 
                if (h_nextstep - h_current) <= 1 and (curr_h, curr_w, dir[0], dir[1]) not in seen and (nex_h, nex_w, -dir[0], -dir[1]) not in seen:
                    seen.append((curr_h, curr_w, dir[0], dir[1]))    
                    steps.append((curr_h, curr_w, count, dir[0], dir[1]))
                    visu.append((curr_h, curr_w))

visu = list(set(visu))
from library.coord_visu import DrawCoordMap
mapt = DrawCoordMap(visu, [S, E])
mapt.draw_map(200)
