from global_ import globalvariables as gv
f = gv.filecontent

items = f.split("\n")

sum = 0
for i in items:
    items_c = len(i)
    half = int(items_c/2)
    f_half = set(i[:half])
    l_half = set(i[half:])
    common = f_half & l_half

    for c in common:
        if ord(c) >= 97: # lowercase
            sum += ord(c) - 96
        else: # uppercase
            sum += ord(c) - 38
    
print(sum)