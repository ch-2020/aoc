import numpy as np
import re
import pprint as pp

class Aplenty:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []

        self.workflows = {}
        self.parts = []

    def run_program(self, mode) -> int:
        self.extract_data(self.filepath)
       
        if mode == "part1":
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self, filepath):
        with open(filepath, "r") as f:
            workflow, parts = f.read().split("\n\n")
            
            for w in workflow.split():
                key = w.split('{')[0]
                rules = w.split('{')[1].split('}')[0].split(',')
                rl = []
                for r in rules:
                    c = re.split('([><:])', r)
                    if len(c) == 5:
                        rl.append((c[0], c[1], int(c[2]), c[4]))
                    else: 
                        rl.append((c[0]))
                self.workflows[key] = rl
            
            for p in parts.split():
                eps = p.split('{')[1].split('}')[0].split(',')
                pl = {}
                for ep in eps:
                    data = ep.split("=")
                    pl[data[0]] = int(data[1])
                self.parts.append(pl)

    def check_part(self, startkey, partsval):
        for r in self.workflows[startkey]:
            if type(r) is str and (r == 'A' or r == 'R'):
                return r
            elif type(r) is str and (r != 'A' and r != 'R'):
                return self.check_part(r, partsval)
            elif len(r) == 4:
                if r[1] == '>':
                    condition = partsval[r[0]] > r[2]
                elif r[1] == '<':
                    condition = partsval[r[0]] < r[2]
                #condition
                if condition and (r[3] == 'A' or r[3] == 'R'):
                    return r[3]
                elif condition and (r[3] != 'A' and r[3] != 'R'):
                    return self.check_part(r[3], partsval)
                elif condition == False: 
                    continue

    def check_ranges(self, ranges, name = "in"):
        if name == "R": # if reject -> not considered
            return 0
        if name == "A": # if accept -> calculate 
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product
        
        fallback = self.workflows[name][-1]
        rules = [x for x in self.workflows[name][:-1]]

        total = 0
        for key, cmp, n, target in rules:
            lo, hi = ranges[key]
            if cmp == "<":
                T = (lo, n - 1)
                F = (n, hi)
            else: 
                T = (n + 1, hi)
                F = (lo, n)
            if T[0] <= T[1]: # if true -> recursive to the next one
                copy = dict(ranges)
                copy[key] = T
                total += self.check_ranges(copy, target)
            if F[0] <= F[1]: # if false -> check next rule
                ranges = dict(ranges)
                ranges[key] = F
            else:
                break
        else: # if nothing break, this means that there is value left -> go to fallback
            total += self.check_ranges(ranges, fallback)
        return total

    def part1_solution(self) -> int:
        self.sum = 0
        for part in self.parts:
            res = self.check_part("in", part)
            if res == 'A':
                self.sum += sum(x for x in part.values())
        return self.sum

    def part2_solution(self) -> int:
        self.sum = 0
        return self.check_ranges({key: (1, 4000) for key in "xmas"})

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = Aplenty("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 19114 == test_obj.run_program("part1"),
            'test_2': 167409079868000 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Aplenty("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 575412 part2: 126107942006821