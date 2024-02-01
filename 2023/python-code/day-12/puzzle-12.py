# Part1/2: done with reference to https://www.youtube.com/watch?v=g3Ms5e7Jdqo&ab_channel=HyperNeutrino

import numpy as np
import pprint

class HotSpring:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []
        self.sum = 0

        self.cache = {}

    def run_program(self, mode) -> int:
        self.extract_data()
        if mode == "part1":
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.update_data()
            self.sum = self.part1_solution()
        return self.sum

    def update_data(self):
        temp = []
        for cfg, nums in self.extracted_data:
            new_num = nums * 5
            new_cfg = ('?').join([cfg] * 5)
            temp.append((new_cfg, new_num))
        self.extracted_data = temp

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                cfg, ids = l.split(' ')
                ids = tuple(map(int, ids.split(',')))
                self.extracted_data.append((cfg, ids))
        pprint.pprint(self.extracted_data)

    def count(self, cfg, num):
        if cfg == '':
            return 1 if num == () else 0
        if num == ():
            return 0 if '#' in cfg else 1
        
        key = (cfg, num)
        if key in self.cache:
            return self.cache[key]

        result = 0
        if cfg[0] in '.?': #assume the case where ? is .
            result += self.count(cfg[1:], num)
        if cfg[0] in '#?': #assume the case where ? is #
            if num[0] <= len(cfg) and '.' not in cfg[:num[0]] and (num[0] == len(cfg) or cfg[num[0]] not in '#'):
                result += self.count(cfg[num[0]+1:], num[1:])
        
        self.cache[key] = result
        return result

    def part1_solution(self) -> int:
        self.sum = 0
        for k, p in enumerate(self.extracted_data):
            self.sum += self.count(p[0], p[1])
            print(f'--- {k}/{len(self.extracted_data)}')
        return self.sum

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = HotSpring("puzzle-test.txt")
        test_obj2 = HotSpring("puzzle-test.txt")
        unittest_dataprocessing = { 
            #'test_1': 21 == test_obj.run_program("part1"),
            'test_2': 525152 == test_obj2.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = HotSpring("puzzle-day-12-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 7718