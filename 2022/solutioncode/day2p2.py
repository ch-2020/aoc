from global_ import globalvariables as gv
f = gv.filecontent
from global_ import globalvariables as gv
f = gv.filecontent

score = {
    "ro": 1,
    "pa": 2,
    "sc": 3, 
    "lose": 0,
    "draw": 3,
    "win": 6 
}

sign = {
    "A": "ro",
    "B": "pa",
    "C": "sc"
}

losing = {
    "pa": "ro",
    "ro": "sc",
    "sc": "pa"
}

winning = {
    "pa": "sc",
    "ro": "pa",
    "sc": "ro"
}

games = f.split("\n")

sum = 0
for g in games:
    opp, own = g.split(" ")
    opp = sign[opp]
    if own == "X":
        sum += score["lose"] + score[losing[opp]]
    elif own == "Y":
        sum += score["draw"] + score[opp]
    elif own == "Z":
        sum += score["win"] + score[winning[opp]]

print(sum)

