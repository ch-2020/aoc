import pprint as pp

class LavaductLagoon:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

        #part1
        self.coords = []

        #part2
        self.new_codes = []

    def run_program(self, mode) -> int:
        if mode == "part1":
            self.extract_data()
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.extracted_data = []
            self.extract_data()
            self.extract_code()
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                d, n, c = l.strip().split()
                num = int(n)
                color = c.split('(')[1].split(')')[0]
                self.extracted_data.append((d, num, color))
    
    def extract_code(self):
        newd = {'0': "R", '1': "D", '2': "L", '3': "U"}
        for d, n, color in self.extracted_data:
            direction = [*color][-1]
            number = int(''.join([*color][1:6]), 16)
            self.new_codes.append((newd[direction], number))
        pp.pprint(self.new_codes)

    def find_area(self, coords, boundary):
        # shoelace formula (however, it is using the middle points)
        A = abs(sum(coords[i][0] * (coords[i - 1][1] - coords[(i + 1) % len(coords)][1]) for i in range(len(coords)))) / 2
        
        # pick's theoerem (consider boundary and inner parts)
        # A = i + B/2 - 1
        i = A - (boundary/2) + 1
        return int(i + boundary)

    def generate_boundary(self, data):
        start = (0,0)
        r, c = start
        coords = [(0,0)]

        dir = {"U": (-1, 0), 'D': (1, 0), "L": (0, -1), "R": (0, 1)}
        boundary = 0
        for d in data:
            boundary += d[1]
            r = r + dir[d[0]][0] * d[1]
            c = c + dir[d[0]][1] * d[1]
            coords.append((r, c))
        return coords, boundary

    def part1_solution(self) -> int:
        self.coords, boundary = self.generate_boundary(self.extracted_data)
        area = self.find_area(self.coords, boundary)
        return area

    def part2_solution(self) -> int:
        self.coords, boundary = self.generate_boundary(self.new_codes)
        area = self.find_area(self.coords, boundary)
        return area

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = LavaductLagoon("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 62 == test_obj.run_program("part1"),
            'test_2': 952408144115 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = LavaductLagoon("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') # part1: 48652 # part2: 45757884535661