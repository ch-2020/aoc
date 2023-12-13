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

    def check_difference(self, l1, l2) -> int:
        diff = 0
        for num, cha in enumerate(l1):
            if l1[num] != l2[num]:
                diff += 1
        return diff
    
    def fix_smudge(self, block):
        # --- TO DO ---
        b_tmp = block
        updated = False
        #check horizontal
        for k_i, i in enumerate(block):
            for k_j, j in enumerate(block):
                if k_i != k_j:
                    if self.check_difference(i, j) == 1:
                        b_tmp[k_i] = ['#']*len(block[0])
                        b_tmp[k_j] = ['#']*len(block[0])
                        updated = True
                        break
        #check vertical
        if updated == False:
            b_tmp = np.transpose(block).tolist()
            for k_i, i in enumerate(block):
                for k_j, j in enumerate(block):
                    if k_i != k_j:
                        if self.check_difference(i, j) == 1:
                            b_tmp[k_i] = ['#']*len(block[0])
                            b_tmp[k_j] = ['#']*len(block[0])
                            break
            b_tmp = np.transpose(b_tmp).tolist()
        block = b_tmp
        return block

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
        # --- TO DO ---
        self.sum = 0
        for k, b in enumerate(self.extracted):
            #update the smudge
            b_updated = self.fix_smudge(b)
            pprint.pprint(b)
            pprint.pprint(b_updated)

            input()
            #search mirror as in solution 1
        

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = Mirrors("puzzle-test.txt")
        unittest_dataprocessing = { 
            #'test_1': 405 == test_obj.run_program("part1"),
            'test_1': 400 == test_obj.run_program("part2"),
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Mirrors("puzzle-day-13-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part1: 29213