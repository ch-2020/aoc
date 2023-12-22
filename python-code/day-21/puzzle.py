import numpy as np

class StepCounter:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []
        self.startpose = ()
        self.rocks = []

    def run_program(self, mode, steps) -> int:
        self.extract_data()
        self.search_start()
        self.search_rocks()

        if mode == "part1":
            self.sum = self.part1_solution(steps)
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                puz = [x for x in [*l.strip()]]
                self.extracted_data.append(puz)
    
    def search_start(self):
        for r in range(len(self.extracted_data)):
            for c in range(len(self.extracted_data[0])):
                if self.extracted_data[r][c] == "S":
                    self.startpose = (r, c)
                    break

    def search_rocks(self):
        for r in range(len(self.extracted_data)):
            for c in range(len(self.extracted_data[0])):
                if self.extracted_data[r][c] == "#":
                    self.rocks.append((r, c))

    def part1_solution(self, steps) -> int:
        self.currenttile = set()
        self.currenttile.add(self.startpose)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for _ in range(steps):
            tiles_current = set(self.currenttile)           
            tiles_next = set()
            for tr, tc in tiles_current:
                for r, c in directions:
                    nr = tr + r
                    nc = tc + c
                    if (nr, nc) not in self.rocks:
                        tiles_next.add((nr, nc))
            self.currenttile = set(tiles_next)
        covered = len(self.currenttile)
        return covered     

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = StepCounter("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 16 == test_obj.run_program("part1", 6),
            'test_2': 16733044 == test_obj.run_program("part2", 5000),
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    elif mode == "part1":
        func_obj = StepCounter("puzzle-input.txt")      
        sum = func_obj.run_program("part1", 64)    
        print(f'Total number is {sum}') #part1: 3733

    elif mode == "part2":
        func_obj = StepCounter("puzzle-input.txt")      
        sum = func_obj.run_program("part2", 26501365)    
        print(f'Total number is {sum}') #part2:
