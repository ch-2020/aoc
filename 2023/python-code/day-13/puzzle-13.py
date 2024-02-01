import numpy as np
import copy

class Mirrors:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted = []
        self.sum_key = {}

    def run_program(self, mode) -> int:
        if mode == "part1":
            self.extract_data()
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.extracted = []
            self.extract_data()
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
                    elif '?' in [m[c-1-up], m[c+2+up]]:
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

    def check_mirror_ignore_prev(self, m, ign):
        similar = None
        pointer = None
        isFound = False
        for c in range(0, len(m)-1):
            if ign == None or c != (ign-1):
                if m[c] == m[c+1]:
                    for up in range(0, min(c, len(m)-2-c)):
                        if m[c-1-up] == m[c+2+up]:
                            similar = True
                        elif '?' in [m[c-1-up], m[c+2+up]]:
                            similar = True
                        else:
                            similar = False
                    if c == len(m)-2 or c == 0:
                        similar = True
                    if similar:
                        isFound = True
                        pointer = c + 1
                        return isFound, pointer
                else:
                    continue

        return isFound, pointer 
        
    def check_difference(self, l1, l2):
        diff = 0
        key = 0
        for num, cha in enumerate(l1):
            if l1[num] != l2[num]:
                diff += 1
                key = num
        return (diff, key)
    
    def fix_smudge(self, block, blockid):
        b_tmp = block.copy()
        updated = False
        #check horizontal
        for k_i, i in enumerate(block):
            for k_j, j in enumerate(block):
                if k_i != k_j:
                    (d, k) = self.check_difference(i, j)
                    if d == 1:
                        c1 = b_tmp[k_i][k]
                        c2 = b_tmp[k_j][k]
                        b_tmp[k_i][k]= '?'
                        b_tmp[k_j][k]= '?'

                        if self.sum_key[blockid][0] == 'H':
                            isF, key = self.check_mirror_ignore_prev(b_tmp, self.sum_key[blockid][1])
                            isF2, key2 = self.check_mirror_ignore_prev(np.transpose(b_tmp).tolist(), None)
                        else:
                            isF, key = self.check_mirror_ignore_prev(b_tmp, None)
                            isF2, key2 = self.check_mirror_ignore_prev(np.transpose(b_tmp).tolist(), self.sum_key[blockid][1])

                        if (isF and ('H', key) != self.sum_key[blockid]) or (isF2 and ('V', key2) != self.sum_key[blockid]): # found mirror
                            print(f'---- HOR changed: {k_i},{k} & {k_j},{k} ----')
                            return b_tmp
                        else: #revert and continue
                            b_tmp[k_i][k] = c1
                            b_tmp[k_j][k] = c2
                else:
                    continue
            else:
                continue
        #check vertical
        if updated == False:
            b_tmp = np.transpose(block).tolist()
            for k_i, i in enumerate(b_tmp):
                for k_j, j in enumerate(b_tmp):
                    if k_i != k_j:
                        (d, k) = self.check_difference(i, j)
                        if d == 1:
                            c1 = b_tmp[k_i][k]
                            c2 = b_tmp[k_j][k]
                            b_tmp[k_i][k]= '?'
                            b_tmp[k_j][k]= '?'
                                   
                            if self.sum_key[blockid][0] == 'V':
                                isF, key = self.check_mirror_ignore_prev(b_tmp, self.sum_key[blockid][1])
                                isF2, key2 = self.check_mirror_ignore_prev(np.transpose(b_tmp).tolist(), None)
                            else:
                                isF, key = self.check_mirror_ignore_prev(b_tmp, None)
                                isF2, key2 = self.check_mirror_ignore_prev(np.transpose(b_tmp).tolist(), self.sum_key[blockid][1])

                            if (isF and ('V', key) != self.sum_key[blockid]) or (isF2 and ('H', key2) != self.sum_key[blockid]): # found mirror
                                print(f'---- VER changed: {k_i},{k} & {k_j},{k} ----')
                                b_tmp = np.transpose(b_tmp).tolist()
                                return b_tmp
                            else: #revert and continue
                                b_tmp[k_i][k] = c1
                                b_tmp[k_j][k] = c2
                    else:
                        continue
                else:
                    continue
            b_tmp = np.transpose(b_tmp).tolist()
        return b_tmp

    def part1_solution(self) -> int:
        self.sum = 0

        for k, b in enumerate(self.extracted):
            #try horizontal
            isFound, pointer = self.check_mirror(b)
            if isFound:
                total = 100*pointer
                self.sum += total
                self.sum_key[k] = ('H', pointer)
            #try vertical
            else:
                m_t = np.transpose(b).tolist()
                isFound, pointer = self.check_mirror(m_t)
                self.sum += pointer
                self.sum_key[k] = ('V', pointer)
        return self.sum

    def part2_solution(self) -> int:
        self.sum = 0
        for k, b in enumerate(self.extracted):
            #update the smudge
            b_updated = copy.deepcopy(b)
            b_updated = self.fix_smudge(b_updated, k)

            #search mirror as in solution 1
            #try horizontal
            if self.sum_key[k][0] == 'H':
                isFound, pointer = self.check_mirror_ignore_prev(b_updated, self.sum_key[k][1])
            else:
                isFound, pointer = self.check_mirror_ignore_prev(b_updated, None)

            if isFound:
                self.sum += 100*pointer
            #try vertical
            else:
                m_t = np.transpose(b_updated).tolist()
                if self.sum_key[k][0] == 'V':
                    isFound, pointer = self.check_mirror_ignore_prev(m_t, self.sum_key[k][1])
                else:
                    isFound, pointer = self.check_mirror_ignore_prev(m_t, None) 
                self.sum += pointer
            print(f'---- Block {k}: {self.sum} ----')
        return self.sum 

if __name__ == "__main__":
    mode = "solution" #"solution", "test"

    if mode == "test":     
        test_obj = Mirrors("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 405 == test_obj.run_program("part1"),
            'test_2': 400 == test_obj.run_program("part2"),
            'test_diff': (1, 8) == test_obj.check_difference(['.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#'], ['.', '#', '#', '#', '#', '.', '.', '#', '.', '#', '#'])
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Mirrors("puzzle-day-13-input.txt")      
        sum = func_obj.run_program("part1")    
        print(f'P1: Total number is {sum}') # part1: 29213
        sum = func_obj.run_program("part2")    
        print(f'P2: Total number is {sum}') # part2: 37453