import numpy as np
import pprint as pp
from collections import deque
import numpy as np

class PulsePropagation:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []

        self.extracted_data = {}
        self.dict_modules = {} # % name: value (1: on, 0: off) & name: memory [1,0,1,0...]
        
        self.q = deque()

    def run_program(self, mode) -> int:
        self.extract_data()
        self.init_modules()
        if mode == "part1":
            self.sum = self.part1_solution()

        elif mode == "part2":
            self.sum = self.part2_solution()
        return self.sum
    
    # extract modules from 
    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                items = l.strip().split(' -> ')
                key = items[0]
                dest_list = items[1].split(", ")
                if key == "broadcaster":
                    self.extracted_data[key] = ("", dest_list)
                else:
                    self.extracted_data[key[1:]] = (key[0], dest_list)

    # initialize dict_modules
    def init_modules(self):
        for name in self.extracted_data:
            val = self.extracted_data[name]
            if name == "broadcaster":
                pass
            elif val[0] == "%": #flip flop
                self.dict_modules[name] = 0
            elif val[0] == "&": #conjuction
                self.dict_modules[name] = {}
                for data in self.extracted_data:
                    tp, des = self.extracted_data[data]
                    if name in des:
                        self.dict_modules[name][data] = 0

    def flipflop(self, name, pulse):
        if pulse == 1:
            return None #ignore
        else:
            if self.dict_modules[name] == 1:
                self.dict_modules[name] = 0
                return 0
            else:
                self.dict_modules[name] = 1
                return 1
    
    def conjuction(self, prev, name, pulse):
        if self.dict_modules[name] == {}: #init
            self.dict_modules[name] = {prev: pulse}
            if pulse == 1:
                return 0
            else:
                return 1
        elif prev not in list(self.dict_modules.keys()):
            self.dict_modules[name][prev] = pulse
            if pulse == 1:
                return 0
            else:
                return 1
        else:
            self.dict_modules[name][prev] = pulse
            if all(list(self.dict_modules[name].values())) == 1:
                return 0
            else:
                return 1

    '''
    This cast_per_click function no longer valid
    because recursive function does not handle the 
    required processing sequence (deque will handle 
    it accordingly)'''
    def cast_per_click(self, prev, key, pulse):
        h = 0
        l = 0
        sumh = 0
        suml = 0

        if pulse == None or key not in list(self.extracted_data.keys()):
            return (0, 0)
        
        if key == "broadcaster":
            for d in self.extracted_data[key][1]:
                h += 1 if pulse == 1 else 0
                l += 1 if pulse == 0 else 0
                (sumh, suml) = self.cast_per_click(key, d, pulse)
                h += sumh
                l += suml
        else: 
            if self.extracted_data[key][0] == "%":
                sig = self.flipflop(key, pulse)
            else: 
                sig = self.conjuction(prev, key, pulse)
            for d in self.extracted_data[key][1]:
                h += 1 if sig == 1 else 0
                l += 1 if sig == 0 else 0
                (sumh, suml) = self.cast_per_click(key, d, sig)
                h += sumh
                l += suml
        return (h, l)

    def cast_with_queue(self, loop):
        hi = lo = 0

        for _ in range(loop):
            lo += 1
            self.q = deque([("broadcaster", x, 0) for x in self.extracted_data["broadcaster"][1]])
            while self.q:
                prev, dest, pulse = self.q.popleft()

                if pulse == 0:
                    lo += 1
                elif pulse == 1:
                    hi += 1
                
                if pulse == None or dest not in list(self.extracted_data.keys()):
                    continue
                
                if self.extracted_data[dest][0] == "%":
                    sig = self.flipflop(dest, pulse)
                    for d in self.extracted_data[dest][1]:
                        self.q.append((dest, d, sig))
                else: 
                    sig = self.conjuction(prev, dest, pulse)
                    for d in self.extracted_data[dest][1]:
                        self.q.append((dest, d, sig))
        sum = lo * hi
        return sum

    def cast_search_rx_low(self, tries):
        loop = 0
        (source, ) = (x for x in self.extracted_data.keys() if self.extracted_data[x][1] == ["rx"])
        source2 = [x for x in self.extracted_data.keys() if source in self.extracted_data[x][1]]
        counter = {s: 0 for s in source2}

        for _ in range(tries):
            loop += 1
            self.q = deque([("broadcaster", x, 0) for x in self.extracted_data["broadcaster"][1]])
            while self.q:
                prev, dest, pulse = self.q.popleft()

                if pulse == None or dest not in list(self.extracted_data.keys()):
                    continue
                
                if self.extracted_data[dest][0] == "%":
                    sig = self.flipflop(dest, pulse)
                    for d in self.extracted_data[dest][1]:
                        self.q.append((dest, d, sig))
                        
                else: 
                    sig = self.conjuction(prev, dest, pulse)
                    for d in self.extracted_data[dest][1]:
                        self.q.append((dest, d, sig))
                        if sig == 1 and dest in source2:
                            c = counter[dest]
                            if c == 0:
                                counter[dest] = loop
                            elif loop % c != 0:
                                counter[dest] = loop
                            
        return counter
                        

    def part1_solution(self) -> int:
        sum = self.cast_with_queue(10000)
        return sum

    def part2_solution(self) -> int:
        counter = self.cast_search_rx_low(10000)
        res = list(counter.values())
        print(res)
        num = np.lcm.reduce(res)
        return num

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = PulsePropagation("puzzle-test.txt")
        test_obj2 = PulsePropagation("puzzle-test2.txt")

        unittest_dataprocessing = { 
            'test_2': 32000000 == test_obj2.run_program("part1"),
            'test_1': 11687500 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = PulsePropagation("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part1: 812721756, # part2: 233338595643977