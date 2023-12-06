import sys, os
import numpy as np

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class BoatRace:
    def __init__(self, inputs) -> None:
        self.inputs = inputs
        self.matches = []

    def run_program(self, mode) -> int:
        if mode == "part1":
            self.part1_generate_items()
            return self.solution()
              
        elif mode == "part2":
            self.part2_generate_items()
            return self.solution()
            

    def part2_generate_items(self):
        time = int("".join(list(self.inputs[0].split(":")[1].split())))
        dist = int("".join(list(self.inputs[1].split(":")[1].split())))

        self.matches.append([time, dist])

    def part1_generate_items(self):
        times = list(map(int, self.inputs[0].split(":")[1].split()))
        dists = list(map(int, self.inputs[1].split(":")[1].split()))
        for i in range(0, len(times)):
            self.matches.append([times[i], dists[i]])
    
    def solution(self): 
        success_tries = []
        total_sum = 0
        for match in self.matches:
            count_benchmark = 0
            t = match[0]
            d = match[1]

            for p in range(0, t + 1):
                dist = (t - p) * (p)
                if dist <= d:
                    count_benchmark += 1
                else:
                    break
            success_num = (t + 1) - 2 * count_benchmark
            success_tries.append(success_num)
  
        total_sum = np.prod(np.array(success_tries))  
        print(f'{success_tries}: {total_sum}')
        return total_sum


if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":
        test_filepath = os.path.join(os.path.dirname(__file__), 'puzzle-test.txt')
        test_lines = ReadFileObject().get_lines_from_file(test_filepath)
        
        test_obj = BoatRace(test_lines[1])
        unittest_dataprocessing = { 
            'test_1': 288 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-6-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:
            func_obj = BoatRace(lines[1])
            sum = func_obj.run_program(mode)
            print(f'Total number is {sum}')

        else:
            print("Error when opening file!")
        
    