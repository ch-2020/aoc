import numpy as np

class Snowverload:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

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
            for l in self.inputs:
                puz = [x for x in [*l]]
                self.extracted_data.append(puz)

    def part1_solution(self) -> int:
       pass

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = Snowverload("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 54 == test_obj.run_program("part1")
            #'test_2': 8 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Snowverload("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}')