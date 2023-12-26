import numpy as np
from itertools import combinations, count
from sympy import symbols, Eq, solve
import time

class Hail:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

    def run_program(self, mode, low = 0, high = 0) -> int:
        self.extract_data()
       
        if mode == "part1":
            self.sum = self.part1_solution(low, high)
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                puz = list(map(int, l.strip().replace("@", ",").split(",")))
                self.extracted_data.append(puz)

    def will_intersect(self, h1, h2, rangelow, rangehigh):
        px, py, pz, vx, vy, vz = h1
        px2, py2, pz2, vx2, vy2, vz2 = h2

        #check if parallel
        par = np.cross([vx, vy], [vx2, vy2])
        if par == 0:
            return False
        elif (px2 > px and vx2 > 0 and vx < 0) or (px > px2 and vx > 0 and vx2 < 0):
            return False
        elif (py2 > py and vy2 > 0 and vy < 0) or (py > py2 and vy > 0 and vy2 < 0):
            return False
        else:
            ta, tb = symbols('ta tb')
            eq1 = Eq((-ta * vx) + (tb * vx2), px - px2)
            eq2 = Eq((-ta * vy) + (tb * vy2), py - py2)
            res = solve((eq1, eq2), (ta, tb))

            ix = float(px + res[ta] * vx)
            iy = float(py + res[ta] * vy)
            if float(res[ta]) > 0 and float(res[tb]) > 0 and ix >= rangelow and ix <= rangehigh and iy >= rangelow and iy <= rangehigh:
                return True
            else:
                return False

    def part1_solution(self, low, high) -> int:
        combi = combinations(self.extracted_data, 2)
        sum = 0
        for i, c in enumerate(combi):
            #print(f'.... {i} ....')
            intersect = self.will_intersect(c[0], c[1], low, high)
            if intersect:
                sum += 1
        return sum

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = Hail("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 2 == test_obj.run_program("part1", 7, 27),
            'test_2': 47 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    elif mode == "part1":
        func_obj = Hail("puzzle-input.txt")   
        print(f'started ....')
        start = time.time()   
        sum = func_obj.run_program(mode, 200000000000000, 400000000000000)    
        end = time.time()
        print(f'Total time is {end - start}')
        print(f'Total number is {sum}') # part1: 13965

    elif mode == "part2":
        func_obj = Hail("puzzle-input.txt")   
        print(f'started ....')
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part2: 