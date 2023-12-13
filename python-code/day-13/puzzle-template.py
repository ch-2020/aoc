import numpy as np
import pprint

class Mirrors:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted = []

    def run_program(self, mode) -> int:
        self.extract_data()
       
        if mode == "part1":
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            blocks = f.read().split("\n\n")
            for b in blocks:
                b_m = []
                lines = b.split("\n")
                for l in lines:
                    b_m.append([x for x in l])
                self.extracted.append(b_m)

    def check_mirror(self, m):
        similar = None
        pointer = 0
        isFound = False
        for c in range(0, len(m)-1):
            if m[c] == m[c+1]:
                for up in range(0, min(c, len(m)-2-c)):
                    if m[c-1-up] == m[c+2+up]:
                        similar = True
                    else:
                        similar = False
                        break
                if c == len(m)-2 or c == 0:
                    similar = True
                if similar:
                    pointer = c + 1
                    isFound = True
                    return isFound, pointer
        else:
            return isFound, pointer

    def part1_solution(self) -> int:
        self.sum = 0

        for k, b in enumerate(self.extracted):
            #try horizontal
            isFound, pointer = self.check_mirror(b)
            if isFound:
                self.sum += 100*pointer
            #try vertical
            else:
                m_t = np.transpose(b).tolist()
                isFound, pointer = self.check_mirror(m_t)
                self.sum += pointer
        return self.sum

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "part1" #"part2", "test"

    if mode == "test":     
        test_obj = Mirrors("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 405 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Mirrors("puzzle-day-13-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part1: 29213