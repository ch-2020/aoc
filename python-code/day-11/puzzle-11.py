import numpy as np
import pprint
from itertools import combinations

class CosmicExpansion:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []
        self.sum = 0
        #part1
        self.expanded = []
        #part2
        self.row_expands = []
        self.column_expands = []
        

    def run_program(self, mode) -> int:
        self.extract_data()
       
        if mode == "part1":
            self.expand_data()
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.get_expansion_data()
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                self.extracted_data.append([x for x in l.strip()])

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

    def get_expansion_data(self):
        for k_l, l in enumerate(self.extracted_data):
            if all(x!='#' for x in l[:]):
               self.row_expands.append(k_l)
        
        for i in range(len(self.extracted_data[0])):
            for k_t, t in enumerate(self.extracted_data):
                if all(x[i]!='#' for x in self.extracted_data):
                    self.column_expands.append(i)
                    break
            
    def generate_unique_pairs(self, data):
        self.coords = []
        for k_l, l in enumerate(data):
            for k_c, c in enumerate(l):
                if c == "#":
                    self.coords.append([k_l, k_c])

        pairs = [comb for comb in combinations(self.coords, 2)]
        return pairs

    def part1_solution(self) -> int:
        pairs = self.generate_unique_pairs(self.expanded)
        self.sum = 0
        for p in pairs:
            temp_sum = abs(p[1][1] - p[0][1]) +  (p[1][0] - p[0][0])
            self.sum += temp_sum
        
        print(self.sum)
        return self.sum

    def part2_solution(self) -> int:
        pairs = self.generate_unique_pairs(self.extracted_data)
        self.sum = 0
        for p in pairs:
            r1 = p[0][0]
            r2 = p[1][0]
            c1 = p[0][1]
            c2 = p[1][1]
            row_range = (min(r1, r2), max(r1, r2))
            col_range = (min(c1, c2), max(c1, c2))

            expanded_row_number = sum(row_range[0] < x < row_range[1] for x in self.row_expands)
            expanded_col_number = sum(col_range[0] < x < col_range[1] for x in self.column_expands)
            steps_row = ((row_range[1] - row_range[0]) - expanded_row_number) + (expanded_row_number * 1000000)
            steps_col = ((col_range[1] - col_range[0]) - expanded_col_number) + (expanded_col_number * 1000000)
            self.sum += steps_row + steps_col
        print(self.sum)
        return self.sum

if __name__ == "__main__":
    mode = "test" #"part2", "test"

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
        print(f'Total number is {sum}') #part1: 9805264 / part2: 779032247216