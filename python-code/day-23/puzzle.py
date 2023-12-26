import numpy as np
from heapq import heappop, heappush

class LongWalk:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []
        self.dir_dict = {
            "<": [(0, -1)],
            ">": [(0, 1)],
            "v": [(1, 0)],
            "^": [(-1, 0)],
            ".": [(0, 1), (1, 0), (0, -1), (-1, 0)],
            "#": []
        }

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
                puz = list(l.strip())
                self.extracted_data.append(puz)

    def part1_solution(self) -> int:
        steps = []
        seen = set()

        first = set()
        for num, c in enumerate(self.extracted_data[0]):
            if c == ".":
                first = (0, 0, num, 1, 0)

        last = ()
        for num, c in enumerate(self.extracted_data[-1]):
            if c == ".":
                last = (len(self.extracted_data) - 1, num)

        pq = [first]
        while pq:
            n, r, c, dr, dc = heappop(pq)
            
            if (r, c) == last: 
                steps.append(-n)
                continue
            
            if (r, c, dr, dc, n) in seen:
                continue
                
            seen.add((n, r, c, dr, dc))

            if self.extracted_data[r][c] in "<>^v":
                ndr, ndc = self.dir_dict[self.extracted_data[r][c]][0]
                nr = r + ndr
                nc = c + ndc
                heappush(pq, (n - 1, nr, nc, ndr, ndc))
                continue
            else:
                for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ndr, ndc) != (-dr, -dc):
                        nr = r + ndr
                        nc = c + ndc
                        if 0 <= nr < len(self.extracted_data) and 0 <= nc < len(self.extracted_data[0]):
                            cha = self.extracted_data[nr][nc]
                            if cha == "#":
                                continue
                            elif cha in "<>^v" and self.dir_dict[cha][0] == (-ndr, -ndc):
                                continue
                            else:
                                heappush(pq, (n - 1, nr, nc, ndr, ndc))
        return max(steps)

    def part2_solution(self) -> int:
        # tutorial based on https://www.youtube.com/watch?v=NTLYL7Mg2jU
        pass
           
        
if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = LongWalk("puzzle-test.txt")
        unittest_dataprocessing = { 
            #'test_1': 94 == test_obj.run_program("part1")
            'test_2': 154 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = LongWalk("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}')