from global_ import globalvariables as gv
f = gv.filecontent
lines = f.split("\n")
rows = len(lines)
cols = len(lines[0])

def search_can_see(val, s):
    count = 0
    for cha in s:
        if int(cha) < val:
            count += 1
        else:
            count += 1
            break
    return count

maxsum = 0
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        current_v = lines[r][c]
        left = lines[r][0:c][::-1]
        right = lines[r][c+1:]
        
        cur_col = ["".join(ele) for v, ele in enumerate(zip(*lines)) if v == c][0]
        top = cur_col[:r][::-1]
        bot = cur_col[r+1:]

        sum = 1
        for x in [top, bot, left, right]:
            sum *= search_can_see(int(current_v), x)
        if sum > maxsum:
            maxsum = sum

print(maxsum)
        

     
