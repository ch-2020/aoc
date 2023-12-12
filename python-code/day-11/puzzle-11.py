import numpy as np
import pprint
from itertools import combinations

class CosmicExpansion:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

        self.expanded = []
        self.sum = 0

    def run_program(self, mode) -> int:
        self.extract_data()
       
        if mode == "part1":
            self.expand_data()
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                self.extracted_data.append([x for x in l.strip()])
        pprint.pprint(self.extracted_data)

    def expand_data(self):
        for l in self.extracted_data:
            if all(x!='#' for x in l[:]):
               self.expanded.append(l)
            self.expanded.append(l)
        
        expanded2 = []
        for i in range(len(self.expanded)):
            expanded2.append(list())

        for i in range(len(self.expanded[0])):
            for k_t, t in enumerate(self.expanded):
                expanded2[k_t].append(t[i])
            if all(x[i]!='#' for x in self.expanded):
                for k_t, t in enumerate(self.expanded):
                    expanded2[k_t].append(t[i])
        self.expanded = expanded2

        pprint.pprint(self.expanded)

    def generate_unique_pairs(self, coords):
        pairs = [comb for comb in combinations(coords, 2)]
        return pairs

    def part1_solution(self) -> int:
        self.coords = []
        for k_l, l in enumerate(self.expanded):
            for k_c, c in enumerate(l):
                if c == "#":
                    self.coords.append([k_l, k_c])

        pairs = self.generate_unique_pairs(self.coords)
        self.sum = 0
        for p in pairs:
            temp_sum = abs(p[1][1] - p[0][1]) +  (p[1][0] - p[0][0])
            self.sum += temp_sum
        
        print(self.sum)
        return self.sum

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "part1" #"part2", "test"

    if mode == "test":     
        test_obj = CosmicExpansion("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 374 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = CosmicExpansion("puzzle-day-11-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}')