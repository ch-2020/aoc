# Solution based on 
# https://www.youtube.com/watch?v=2pDSooPLLkI

from heapq import heappush, heappop
import pprint as pp

class LavaTraffic:
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
        
        print(self.sum)
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                puz = list(map(int, l.strip()))
                self.extracted_data.append(puz)

    def part1_solution(self) -> int:
        # use set when item only added once (no duplicates in set) and order does not matter
        seen = set() 
        #priority queue
        pq = [(0, 0 ,0, 0, 0, 0)] #heatloss, row, column, direction row, direction column, steps

        while pq:
            hl, r, c, dr, dc, n = heappop(pq)

            # break condition (if first time end goal is seen)
            if r == len(self.extracted_data) - 1 and c == len(self.extracted_data[0]) - 1:
                return hl

            # if see similar step, then continue
            if(r, c, dr, dc, n) in seen:
                continue

            seen.add((r, c, dr, dc, n))

            # if next step is valid, then check and update heap
            if n < 3 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(self.extracted_data) and 0 <= nc < len(self.extracted_data[0]):
                    heappush(pq, (hl + self.extracted_data[nr][nc], nr, nc, dr, dc, n + 1))
            
            # if same direction > 3: generate points to check for other directions
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc): # does not allow same direction/reverse
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(self.extracted_data) and 0 <= nc < len(self.extracted_data[0]):
                        heappush(pq, (hl + self.extracted_data[nr][nc], nr, nc, ndr, ndc, 1)) # set n = 1 (first time in the direction)

    def part2_solution(self) -> int:
        # use set when item only added once (no duplicates in set) and order does not matter
        seen = set() 
        #priority queue
        pq2 = [(0, 0 ,0, 0, 0, 0)] #heatloss, row, column, direction row, direction column, steps

        while pq2:
            hl, r, c, dr, dc, n = heappop(pq2)

            # break condition (if first time end goal is seen)
            if r == len(self.extracted_data) - 1 and c == len(self.extracted_data[0]) - 1 and n >= 4: # need also at least 4 to stop
                return hl

            # if see similar step, then continue
            if(r, c, dr, dc, n) in seen:
                continue

            seen.add((r, c, dr, dc, n))

            # if next step is valid, then check and update heap
            if n < 10 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(self.extracted_data) and 0 <= nc < len(self.extracted_data[0]):
                    heappush(pq2, (hl + self.extracted_data[nr][nc], nr, nc, dr, dc, n + 1))
            
            # if same direction > 3: generate points to check for other directions
            if n >= 4 or (dr, dc) == (0, 0):
                for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc): # does not allow same direction/reverse
                        nr = r + ndr
                        nc = c + ndc
                        if 0 <= nr < len(self.extracted_data) and 0 <= nc < len(self.extracted_data[0]):
                            heappush(pq2, (hl + self.extracted_data[nr][nc], nr, nc, ndr, ndc, 1)) # set n = 1 (first time in the direction)


if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = LavaTraffic("puzzle-test.txt")
        unittest_dataprocessing = { 
            #'test_1': 102 == test_obj.run_program("part1"),
            'test_2': 94 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = LavaTraffic("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part1: 1238, part2: 1362