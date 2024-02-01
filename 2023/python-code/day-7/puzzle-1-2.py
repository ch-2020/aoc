import sys, os
from collections import Counter

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class CamelCards:
    def __init__(self, inputs) -> None:
        self.inputs = inputs

        #part1
        self.card_sets = []
        self.sorted_cards = []
        self.sum = 0

        for i in self.inputs:
            substrs = i.strip().split(" ")
            self.card_sets.append([substrs[0], int(substrs[1])])

        #part2
        self.manipulated_card_sets = []
    
    def run_program(self, mode) -> int:
        self.mode = mode
        if mode == "part1":
            #self.init_demo()
            self.part1_solution()
            self.part1_getsum()
            return self.sum

        elif mode == "part2":
            self.part2_get_manipulated()
            self.part2_solution()
            self.part1_getsum()
            return self.sum

    def part2_get_manipulated(self):
        map2 = {v: 13-k for k, v in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])}
        for k, n in self.card_sets:
            replace_k = []
            if 'J' in [*k]:
                type = self._check_cardtype(k)
                if type == 6:
                    replace_k = ['A']*5

                elif type == 5 or type == 4:
                    counter = Counter([*k])
                    map2_s =  sorted(counter, key=counter.get, reverse=True)
                    if map2_s[0] > map2_s[1]:
                        replace_k = [map2_s[0]]*5
                    else:
                        replace_k = [map2_s[1]]*5

                elif type == 3:
                    counter = Counter([*k])
                    map2_s =  sorted(counter, key=counter.get, reverse=True)

                    if counter['J'] == 3:
                        #search for the biggest and replace it
                        if map2_s[1] > map2_s[2]:
                            replace_k = [map2_s[1]]*4 + [map2_s[2]]
                        else:
                            replace_k = [map2_s[2]]*4 + [map2_s[1]]

                    else:
                        for x in [*k]:
                            if x == 'J':
                                replace_k.append(map2_s[0])
                            else:
                                replace_k.append(x)

                elif type == 2:
                    counter = Counter([*k])
                    map2_s =  sorted(counter, key=counter.get, reverse=True)

                    if counter['J'] == 2:
                        max_char = ''
                        for i in map2_s:
                            if i != 'J':
                                max_char = i
                                break
                        replace_k = [max_char]*4 + [map2_s[2]]
                    else:
                        if map2_s[0] > map2_s[1]:
                            replace_k = [map2_s[0]]*3 + [map2_s[1]]*2
                        else:
                            replace_k = [map2_s[1]]*3 + [map2_s[0]]*2
                
                elif type == 1:
                    counter = Counter([*k])
                    map2_s =  sorted(counter, key=counter.get, reverse=True)

                    if counter['J'] == 2:
                        max_num = max([map2[x] for x in list(counter)])
                        max_char = ''
                        for p, v in map2.items():
                            if v == max_num:
                                max_char = p
                                break
                        for x in [*k]:
                            if x == 'J':
                                replace_k.append(max_char)
                            else:
                                replace_k.append(x)
                        
                    else:
                        for x in [*k]:
                            if x == 'J':
                                replace_k.append(map2_s[0])
                            else:
                                replace_k.append(x)

                elif type == 0:
                    counter = Counter([*k])
                    max_num = max([map2[x] for x in list(counter)])
                    max_char = ''
                    for p, v in map2.items():
                        if v == max_num:
                            max_char = p
                            break
                    for x in [*k]:
                        if x == 'J':
                            replace_k.append(max_char)
                        else:
                            replace_k.append(x)
                    
                self.manipulated_card_sets.append([''.join(replace_k), n]) 
            else:
                self.manipulated_card_sets.append([k, n]) 

        return self.manipulated_card_sets

    def part1_solution(self):
        self.sorted_cards = self._quicksort(self.card_sets)

    def part2_solution(self):
        self.sorted_cards = self._quicksort_part2(self.manipulated_card_sets, self.card_sets)

    def part1_getsum(self):
        initnum = 1
        self.sum = 0
        for i in self.sorted_cards:
            self.sum = self.sum + i[1] * initnum
            initnum += 1
        return self.sum

    def _quicksort_part2(self, a_m, a_o):
        blocks = list()
        for i in range(7):
            blocks.append(list())

        for k, v in enumerate(a_m):
            type = self._check_cardtype(v[0])
            blocks[type].append([a_o[k][0], v[1], v[0]])

        sorted_blocks = []
        for k, b in enumerate(blocks):
            if b:
                sorted_blocks += self._quicksort_sametype(b)
 
        return sorted_blocks

    def _quicksort_sametype(self, array):
        if len(array) <= 1:
            return array
        else:
            frontlist = []
            endlist = []
            for x in array[1:]:
                smaller = self._getsmaller_by_order(x[0], array[0][0])
                if smaller == array[0][0]:
                    endlist.append(x)
                else:
                    frontlist.append(x)
            return self._quicksort_sametype(frontlist) + [array[0]] + self._quicksort_sametype(endlist)

    def _quicksort(self, array):
        if len(array) <= 1:
            return array
        else:
            frontlist = []
            endlist = []
            for x in array[1:]:
                if self._check_cardtype(x[0]) < self._check_cardtype(array[0][0]):
                    frontlist.append(x)
                elif self._check_cardtype(x[0]) > self._check_cardtype(array[0][0]):
                    endlist.append(x)
                else: #both are same type
                    smaller = self._getsmaller_by_order(x[0], array[0][0])
                    if smaller == array[0][0]:
                        endlist.append(x)
                    else:
                        frontlist.append(x)

            return self._quicksort(frontlist) + [array[0]] + self._quicksort(endlist)

    def _check_cardtype(self, cards) -> int:
        dict_cardtypes = {
            6: 'five of a kind',    # - five of a kind: 6 (1 set)
            5: 'four of a kind',    # - four of a kind: 5 (2 sets with 4,1)
            4: 'full house',        # - full house:     4 (2 sets with 3,2)
            3: 'three of a kind',   # - three of a kind:3 (3 sets with 3,1,1)
            2: 'two pair',          # - two pair:       2 (3 sets with 2,2,1)
            1: 'one pair',          # - one pair:       1 (4 sets with 2,1,1,1)
            0: 'high card'          # - high card:      0 (5 sets)
        }
        
        char_list = [*cards]
        C = Counter(char_list)
        sub_char_list = [[k,]*v for k, v in C.items()]

        cardtype_id = None
        v = len(sub_char_list)
        if v == 5:
            cardtype_id = 0
        elif v == 4:
            cardtype_id = 1
        elif v == 1: 
            cardtype_id = 6
        elif v == 3: 
            if any([len(sl) == 3 for sl in sub_char_list]) == True:
                cardtype_id = 3
            else:
                cardtype_id = 2
        elif v == 2:
            if any([len(sl) == 4 for sl in sub_char_list]) == True:
                cardtype_id = 5
            else:
                cardtype_id = 4

        return cardtype_id
        
    def _getsmaller_by_order(self, cards1, cards2):
        map_order = {}
        if self.mode == "part1":
            map_order = {v: 13-k for k, v in enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'])}
        elif self.mode == "part2":
            map_order = {v: 13-k for k, v in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])}

        cards1_list = [*cards1]
        cards2_list = [*cards2]

        smaller = cards1
        for k in range(len(cards1_list)):
            if map_order[cards1_list[k]] is not map_order[cards2_list[k]]:
                if map_order[cards1_list[k]] > map_order[cards2_list[k]]:
                    smaller = cards2
                break
        return smaller

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-test.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
     
        test_obj = CamelCards(lines[1])
        unittest_dataprocessing = { 
            'test_2': 5905 == test_obj.run_program("part2"),
            'test_1': 6440 == test_obj.run_program("part1"),
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-7-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:  
            func_obj = CamelCards(lines[1])
            sum = func_obj.run_program(mode)
            print(f'Total number is {sum}') # part 2: 253907829

        else:
            print("Error when opening file!")
        
    