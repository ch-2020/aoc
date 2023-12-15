#https://en.wikipedia.org/wiki/List_of_Unicode_characters
import pprint as pp
import re
import copy
import os, time
from unicodedata import normalize

class ReflectorDish:
    def __init__(self, filepath, visualize = False) -> None:
        self.filepath = filepath
        self.inputs = tuple()
        self.extracted_map = tuple()
        self.moved_map = tuple()
        self.sum = 0
        self.visualize = visualize

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
            self.inputs = tuple(x.strip() for x in f.readlines())
            self.extracted_map = self.transpose_m(self.inputs)

    def transpose_m(self, m):
        transp_map = tuple(map("".join, zip(*reversed(m))))
        return transp_map

    def move_rocks(self, m):
        moved_map = tuple()
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
            moved_map = moved_map + (newsubst,)      
        return moved_map
    
    def calc_load(self, m):
        sum = 0
        for l in m:
            for id, c in enumerate([*l]):
                if c == 'O':
                    sum += (id + 1)
        return sum
        
    def part1_solution(self) -> int:
        self.moved_map = self.move_rocks(self.extracted_map)
        num = self.calc_load(self.moved_map)
        return num

    def part2_solution(self) -> int:
        current_map = copy.deepcopy(self.extracted_map)

        seen = {current_map}
        array = [current_map]

        iter = 0
        while True:
            iter += 1
            north = self.move_rocks(current_map)
            west = self.move_rocks(self.transpose_m(north))
            south = self.move_rocks(self.transpose_m(west))
            east = self.move_rocks(self.transpose_m(south))
            current_map = self.transpose_m(east)
            
            if self.visualize:
                self.visualize_map(north, 'N')
                self.visualize_map(west, 'W')
                self.visualize_map(south, 'S')
                self.visualize_map(east, 'E')

            if current_map in seen:
                break
            seen.add(current_map)
            array.append(current_map)

        first = array.index(current_map)
        grid = array[(1000000000 - first)%(iter - first)+first]

        return self.calc_load(grid)

    def visualize_map(self, m, direc):
        if direc == 'N':
            map = self.transpose_m(self.transpose_m(self.transpose_m(m)))
        elif direc == 'W':
            map = self.transpose_m(self.transpose_m(m))
        elif direc == 'S':
            map = self.transpose_m(m)
        elif direc == 'E':
            map = m

        #visualize
        length = len(map[0])
        print(u'\u250F' + u'\u2501'*length + u'\u2513')
        for m in map:
            show = u'\u2503'
            for c in [*m]:
                if c == '.':
                    show += ' '
                elif c == 'O':
                    show += u'\u25CC'
                elif c == '#':
                    show += u'\u2588'
            show += u'\u2503'
            print(show)
        print(u'\u2517' + u'\u2501'*length + u'\u251B')
        time.sleep(1)
        os.system('clear')
        

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = ReflectorDish("puzzle-test.txt", True)
        unittest_dataprocessing = { 
            #'test_1': 136 == test_obj.run_program("part1"),
            'test_2': 64 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = ReflectorDish("puzzle-day-14-input.txt", True)      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 110821, part2: 83516