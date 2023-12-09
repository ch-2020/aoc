import sys, os
import numpy as np

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class Wasteland:
    def __init__(self, inputs) -> None:
        self.inputs = inputs
        self.start = ""
        self.goal = ""
        self.dir_map = {}
        self.sum = 0

    def run_program(self, mode, start = "", goal = "") -> int:
        self.start = start
        self.goal = goal

        self.extract_data()
        if mode == "part1":
            self.sum = self.part1_solution()
            return self.sum

        elif mode == "part2":
            self.sum = self.part2_solution()
            return self.sum
        
    def extract_data(self):
        self.steps = self.inputs[0].strip()
        direcs = self.inputs[2:]

        for i in direcs:
            key = i.split(" = (")[0]
            left = i.split(" = (")[1].split(", ")[0]
            right = i.split(" = (")[1].split(", ")[1].split(")\n")[0]
            self.dir_map[key] = {"L": left, "R": right}

    def part1_solution(self):
        current_step = self.start
        count = 0
        while current_step != self.goal:
            for s in [*self.steps]:
                try:
                    current_step = self.dir_map[current_step][s]
                    count += 1
                    if current_step == self.goal:
                        break
                except:
                    print(f'**** ERROR: {current_step}: {s}')
        return count

    def part2_solution(self):
        starts = []
        for i in self.dir_map.keys():
            if [*i][2] == 'A':
                starts.append(i)

        ends = []
        for i in self.dir_map.keys():
            if [*i][2] == 'Z':
                ends.append(i)

        z_counts = list()
        for _ in range(len(starts)):
            z_counts.append(list())
        current_steps = starts.copy()

        # Count when a Z is reached
        for st, v in enumerate(current_steps):
            count = 0
            for _ in range(0, 500):
                for s in [*self.steps]:
                    current_steps[st] = self.dir_map[current_steps[st]][s]
                    count += 1
                    if [*current_steps[st]][2] == 'Z':
                        z_counts[st].append(count)
                        break
                else:
                    continue
                break
            else:
                continue
            
        self.sum = np.lcm.reduce(np.array(z_counts, dtype=np.int64))[0]
        return self.sum


if __name__ == "__main__":
    mode = "part2" #"part2", "test"
    filepath = os.path.join(os.path.dirname(__file__), 'puzzle-test.txt')
    lines = ReadFileObject().get_lines_from_file(filepath)

    filepath2 = os.path.join(os.path.dirname(__file__), 'puzzle-test2.txt')
    lines2 = ReadFileObject().get_lines_from_file(filepath2) 
 
    if mode == "test":  
        test_obj = Wasteland(lines[1])
        test_obj2 = Wasteland(lines2[1])
        unittest_dataprocessing = { 
            'test_1': 2 == test_obj.run_program("part1", "AAA", "ZZZ"),
            'test_2': 6 == test_obj2.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-8-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:  
            func_obj = Wasteland(lines[1])
            if mode == "part1":
                sum = func_obj.run_program(mode, "AAA", "ZZZ") #part1: 22199 
            if mode == "part2":
                sum = func_obj.run_program(mode)
            print(f'Total number is {sum}') #part2: 13334102464297

        else:
            print("Error when opening file!")
        
    