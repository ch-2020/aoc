import numpy as np
import re
import pprint as pp
import os, time

class VisuMap:
    def __init__(self, rowlen, collen, dict_mirrors) -> None:
        self.route = []
        self.mirrors = []
        self.dict_mirrors = dict_mirrors
        self.len_row = rowlen
        self.len_col = collen

    def update_mirrors(self, mirrors):
        self.mirrors = list(mirrors)

    def add_point(self, prev, end):
        if prev[0] != end[0]:
            max_num = max(end[0], prev[0])
            min_num = min(end[0], prev[0])
            for i in range(0, max_num-min_num+1):
                newpoint = (min_num+i, prev[1])
                if newpoint not in self.route:
                    self.route.append(newpoint)
        else:
            max_num = max(end[1], prev[1])
            min_num = min(end[1], prev[1])
            for i in range(1, max_num-min_num+1):
                newpoint = (prev[0], min_num+i)
                if newpoint not in self.route:
                    self.route.append(newpoint)
        if prev not in self.route:
            self.route.append(prev)
        if end not in self.route:
            self.route.append(end)
        
    def update(self):
        os.system('clear')
        print(u'\u250F' + u'\u2501' * self.len_col + u'\u2513')
        for r in range(self.len_row):
            show = u'\u2503'
            for c in range(self.len_col):
                if (r,c) not in self.route and (r,c) in self.mirrors:
                    if self.dict_mirrors[(r,c)] == '|':
                        show += u'\u2502'
                    elif self.dict_mirrors[(r,c)] == '\\':
                        show += u'\u2572'
                    elif self.dict_mirrors[(r,c)] == '/':
                        show += u'\u2571'
                    elif self.dict_mirrors[(r,c)] == '-':
                        show += u'\u2500'
                elif (r,c) in self.route and (r,c) in self.mirrors:
                    show += u'\u2592'
                elif (r,c) in self.route and (r,c) not in self.mirrors:
                    show += u'\u2591'
                else:
                    show += ' '
            show += u'\u2503'
            print(show)
        print(u'\u2517' + u'\u2501' * self.len_col + u'\u251B')
        time.sleep(0.3)
        
class LavaFloor:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted = []
        self.len_row = 0
        self.len_col = 0

        self.dict_mirrors = {}
        self.dict_pairs = {}
        self.route = []

        self.showmap = []

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

            self.dict_mirrors[(0,0)] = '-'
            for l_id, l in enumerate(self.inputs):
                self.extracted.append(l.strip())
                l_id += 0
                for c_id, c in enumerate([*l.strip()]):
                    if re.match('[\\\\|\-/]', c):
                        self.dict_mirrors[(l_id, c_id)] = c
            
            self.len_col = len([*self.extracted])
            self.len_row = len(self.extracted)
    
    def print_details(self):
        print(f'rows: {self.len_row}')
        print(f'cols: {self.len_col}')
        print('**** mirrors ****')
        pp.pprint(self.dict_mirrors)
        print('---keys---')
        pp.pprint(self.dict_mirrors.keys())
        print('**** pairs ****')
        pp.pprint(self.dict_pairs)
        print('---keys---')
        pp.pprint(self.dict_pairs.keys())
        print('**** route ****')
        pp.pprint(self.route)
        input()

    def find_next(self, coord, cha):
        row, col = coord

        # CASE 1
        if cha in '-/\\': 
            allmirrors = self.dict_mirrors.keys()

            left = None
            right = None
            same_rows = [x for x in allmirrors if x[0] == row]
            for r, c in same_rows:
                if c!= col and c < col:
                    left = (row, c)
                elif c == col:
                    if left == None and (row, 0) != coord:
                        left = (row, 0)
                    else:
                        break

            for rr, rc in reversed(same_rows):
                if rc != col and rc > col:
                    right = (row, rc)
                elif rc == col:
                    if right == None and (row, self.len_col-1) != coord:
                        right = (row, self.len_col-1)
                    else:
                        break
            
            if left != None:
                try:
                    self.dict_pairs[coord]["left"] = left
                except:
                    self.dict_pairs[coord] = {}
                    self.dict_pairs[coord]["left"] = left
                try:
                    self.dict_pairs[left]["right"] = coord
                except:
                    self.dict_pairs[left] = {}
                    self.dict_pairs[left]["right"] = coord

            if right != None:
                try:
                    self.dict_pairs[coord]["right"] = right
                except:
                    self.dict_pairs[coord] = {}
                    self.dict_pairs[coord]["right"] = right
                try:
                    self.dict_pairs[right]["left"] = coord
                except:
                    self.dict_pairs[right] = {}
                    self.dict_pairs[right]["left"] = coord

        # CASE 2
        if cha in '|/\\':
            top = None
            bot = None

            a = list(zip(*self.extracted))[col]
            b = list(a)

            part = [*reversed(a[:row])]
            for t in range(len(part)): 
                if len(part) == 0:
                    break
                else:
                    if part[t] != '.':
                        top = (row-1-t, col)
                        break
                    elif top == None and (0, col) != coord: 
                        top = (0, col)
            
            partd = b[row+1:]
            for t in range(len(partd)): 
                if len(partd) == 0:
                    break
                else:
                    if partd[t] != '.':
                        bot = (row+1+t, col)
                        break
                    elif bot == None and (row+1+t, col) == (self.len_row-1, col): 
                        bot = (self.len_row-1, col)
            
            if top != None:
                try:
                    self.dict_pairs[coord]["top"] = top
                except:
                    self.dict_pairs[coord] = {}
                    self.dict_pairs[coord]["top"] = top
                try:
                    self.dict_pairs[top]["bot"] = coord
                except:
                    self.dict_pairs[top] = {}
                    self.dict_pairs[top]["bot"] = coord
            if bot != None:
                try:
                    self.dict_pairs[coord]["bot"] = bot
                except:
                    self.dict_pairs[coord] = {}
                    self.dict_pairs[coord]["bot"] = bot
                try:
                    self.dict_pairs[bot]["top"] = coord
                except:
                    self.dict_pairs[bot] = {}
                    self.dict_pairs[bot]["top"] = coord

    def search_route(self, coord, comefrom):
        if coord not in self.dict_pairs.keys() or coord not in self.dict_mirrors.keys():
            return [(coord, comefrom)]
        if coord in self.route:
            return [(coord, comefrom)]
        else: 
            nexts = self.dict_pairs[coord]
            valid = []
            for n in nexts:
                if comefrom == "left":
                    if n == "bot" and self.dict_mirrors[coord] == '\\':
                        valid.append((nexts[n], "top"))
                    elif n == "top" and self.dict_mirrors[coord] == "/":
                        valid.append((nexts[n], "bot"))
                    elif n == "right" and self.dict_mirrors[coord] == "-":
                        valid.append((nexts[n], "left"))
                    elif self.dict_mirrors[coord] == "|":
                        try:
                            valid.append((nexts["bot"], "top"))
                        except:
                            pass
                        try:
                            valid.append((nexts["top"], "bot"))
                        except:
                            pass
                        break

                if comefrom == "top":
                    if n == "right" and self.dict_mirrors[coord] == '\\':
                        valid.append((nexts[n], "left"))
                    elif n == "left" and self.dict_mirrors[coord] == "/":
                        valid.append((nexts[n], "right"))
                    elif n == "bot" and self.dict_mirrors[coord] == "|":
                        valid.append((nexts[n], "top"))
                    elif self.dict_mirrors[coord] == "-":
                        try:
                            valid.append((nexts["right"], "left"))
                        except:
                            pass
                        try:
                            valid.append((nexts["left"], "right"))
                        except:
                            pass
                        break

                if comefrom == "bot":
                    if n == "left" and self.dict_mirrors[coord] == '\\':
                        valid.append((nexts[n], "right"))
                    elif n == "right" and self.dict_mirrors[coord] == "/":
                        valid.append((nexts[n], "left"))
                    elif n == "top" and self.dict_mirrors[coord] == "|":
                        valid.append((nexts[n], "bot"))
                    elif self.dict_mirrors[coord] == "-":
                        try:
                            valid.append((nexts["right"], "left"))
                        except:
                            pass
                        try:
                            valid.append((nexts["left"], "right"))
                        except:
                            pass
                        break
                if comefrom == "right":
                    if n == "top" and self.dict_mirrors[coord] == '\\':
                        valid.append((nexts[n], "bot"))
                    elif n == "bot" and self.dict_mirrors[coord] == "/":
                        valid.append((nexts[n], "top"))
                    elif n == "left" and self.dict_mirrors[coord] == "-":
                        valid.append((nexts[n], "right"))
                    elif self.dict_mirrors[coord] == "|":
                        try:
                            valid.append((nexts["bot"], "top"))
                        except:
                            pass
                        try:
                            valid.append((nexts["top"], "bot"))   
                        except:
                            pass
                        break
            return valid

    def part1_solution(self):
        map = VisuMap(self.len_row, self.len_col, self.dict_mirrors)
        map.update_mirrors(self.dict_mirrors.keys())

        # find pairs of neighbouring items
        for i in self.dict_mirrors:
            self.find_next(i, self.dict_mirrors[i])
        
        nexts = self.search_route((0,0), "left")
        self.route.append(((0,0),'start'))
        map.route.append((0,0))
        # search route
        while len(nexts) > 0: 
            n = nexts.pop()    
            newnexts = self.search_route(n[0], n[1])
            for new in newnexts:
                if new not in self.route and new[1] != '':
                    nexts.append(new)
                self.route.append(new)
                map.add_point(n[0], new[0])
                map.update()
        #self.print_details()
        print(f'Len: {len(map.route)}---{map.route}-----')
        return len(map.route)
        
    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":     
        test_obj = LavaFloor("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 46 == test_obj.run_program("part1"),
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')
    else:
        func_obj = LavaFloor("puzzle-16-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 7307