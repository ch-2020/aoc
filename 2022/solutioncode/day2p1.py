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

poss = [
    {"X": "ro", "Y": "pa", "Z": "sc"},
    {"X": "ro", "Y": "sc", "Z": "pa"},
    {"X": "pa", "Y": "ro", "Z": "sc"},
    {"X": "pa", "Y": "sc", "Z": "ro"},
    {"X": "sc", "Y": "pa", "Z": "ro"},
    {"X": "sc", "Y": "ro", "Z": "pa"}
]

winsets = [("ro", "pa"), ("pa", "sc"), ("sc", "ro")]

def compete(opp, own):
    if opp == own:
        return score["draw"] + score[own]
    elif (opp, own) in winsets:
        return score["win"] + score[own]
    else:
        return score["lose"] + score[own] 

games = f.split("\n")

games_sum = []
for po in poss:
    sum = 0
    for g in games:
        opp, own = g.split(" ")
        sum += compete(sign[opp], po[own])
    games_sum.append(sum)

print(games_sum[0])

