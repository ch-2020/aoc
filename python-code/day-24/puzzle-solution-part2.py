import sympy

file = "puzzle-input.txt"

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(file)]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")
equations = []

for sx, sy, sz, vx, vy, vz in hailstones:
    #time to arrive for both hail and rock is the same, which derives the following conditions in 3D (x=y, y=z)
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

answers = sympy.solve(equations)
sum = answers[0][xr] + answers[0][yr] + answers[0][zr]
print(sum)