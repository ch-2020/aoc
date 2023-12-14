import pprint as pp
import re

class ReflectorDish:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_map = []
        self.moved_map = []
        self.sum = 0

        self.moving_key = {}

    def run_program(self, mode) -> int:
        self.extract_data()
       
        if mode == "part1":
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            maps = []
            for row, l in enumerate(self.inputs):
                m = [x for x in [*l.strip()]]
                maps.append(m)
            self.extracted_map = self.transpose_m(maps)

    def transpose_m(self, m):
        transp_map = list(zip(*m))
        return [''.join(x[::-1]) for x in transp_map]

    def move_rocks(self, m):
        moved_map = []
        
        for line in m:
            if line in self.moving_key:
                newsubst = self.moving_key[line]
            
            else:
                substr = re.split(r'(\#)', line)

                newsubst = ''
                for s in substr:
                    new = ''
                    if '#' in s:
                        new = s
                    else:
                        num = s.count('O')
                        new = '.'*(len(s)-num) + 'O'*num
                    newsubst += new
                    self.moving_key[line] = newsubst
            moved_map.append(newsubst)
        return moved_map
    
    def calc_load(self):
        sum = 0
        for l in self.moved_map:
            for id, c in enumerate([*l]):
                if c == 'O':
                    sum += (id + 1)
        return sum
    
    def part1_solution(self) -> int:
        self.moved_map = self.move_rocks(self.extracted_map)
        pp.pprint(self.extracted_map)
        pp.pprint(self.moved_map)
        num = self.calc_load()
        return num

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "part1" #"part2", "test"

    if mode == "test":     
        test_obj = ReflectorDish("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 136 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = ReflectorDish("puzzle-day-14-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 110821