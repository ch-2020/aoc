from global_ import globalvariables as gv
import pprint as pp
f = gv.filecontent
blocks = f.split("\n\n")

monkeys = []
monkey_items = []
monkey_inspections = []

def operation(old, ops):
    sign = ops[1]
    num1 = ops[0]
    num2 = ops[2]
    if ops[0] == "old":
        num1 = old
    if ops[2] == "old":
        num2 = old

    sum = 0
    if sign == "*":
        sum = int(num1) * int(num2)
    elif sign == "+":
        sum = int(num1) + int(num2)

    return sum

def inspect(monkey):
    id, op, test, t, f = monkey
    tmplist = monkey_items[id].copy()

    for it in monkey_items[id]:
        val = tmplist.pop(0)
        updatedval = operation(val, op)
        # Divide the large number by LCM 
        optval = updatedval % mod

        monkey_inspections[id] += 1            
        if optval % test == 0:
            monkey_items[t].append(optval)
        else:
            monkey_items[f].append(optval)

    monkey_items[id] = []

for b in blocks:
    lines = b.splitlines()
    monkey_id = int(lines[0].split(" ")[1].split(":")[0])
    monkey_item = [int(ele) for ele in lines[1].split(":")[1].split(",")]
    monkey_op = [ele for ele in lines[2].split(" ")[-3:]]
    monkey_test = int(lines[3].split(" ")[-1])
    monkey_true = int(lines[4].split(" ")[-1])
    monkey_false = int(lines[5].split(" ")[-1])

    monkeys.append((monkey_id, monkey_op, monkey_test, monkey_true, monkey_false))
    monkey_items.append(monkey_item)
    monkey_inspections.append(0)

# Divide the large number by LCM 
mod = 1
for id, op, test, t, f in monkeys:
    mod *= test

pp.pprint(monkeys)
pp.pprint(monkey_items)
pp.pprint(monkey_inspections)

diff = [0] * len(monkeys)
repeatingres = []
for i in range(10000):
    for m in monkeys:
        inspect(m)

sortedinsp = sorted(monkey_inspections)[::-1]
print(sortedinsp)
print(sortedinsp[0] * sortedinsp[1])