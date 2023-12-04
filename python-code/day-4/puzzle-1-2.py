import sys, os
import re
import numpy as np

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class ScratchCards:
    def __init__(self, inputs) -> None:
        self.inputs_array = inputs
        self.winning_arrays = []
        self.ans_arrays = []
        self.scratchcard_sum = 0

        #part2
        self.dict_scratchcards = {}

    def run_program(self, partid) -> int:
        if partid == "part1":
            self.split_input_array()
            self.calculate_sum()
        
        elif partid == "part2":
            self.split_input_array()
            self.part2_init_dict()
            self.part2_generate_next_cards()
            self.part2_calculate_sum()

        return self.scratchcard_sum

    def split_input_array(self) -> None:
        for v in self.inputs_array:
            game_str = v.split(": ")[0]
            winning_str = v.split(": ")[1].split(" | ")[0]
            ans_str = v.split(": ")[1].split(" | ")[1]

            self.winning_arrays.append(re.findall('\d+', winning_str))
            self.ans_arrays.append(re.findall('\d+', ans_str))
    
    def calculate_sum(self) -> int:
        self.scratchcard_sum = 0
        for k in range(len(self.winning_arrays)):
            temp_sum = 1
            duplicates = self._get_duplicates(self.winning_arrays[k], self.ans_arrays[k])
            
            if len(duplicates) > 0:
                for _ in range(len(duplicates)-1):
                    temp_sum *= 2
            else: 
                temp_sum = 0
            
            self.scratchcard_sum += temp_sum
        return self.scratchcard_sum

    def _get_duplicates(self, array1, array2):
        return np.intersect1d(array1, array2)

    def _get_duplicates_length(self, array1, array2):
        index = [i for i, v in enumerate(array1) if array1.count(v) == array2.count(v)]
        return len(index) 

    def part2_init_dict(self) -> dict:
        for l in range(len(self.inputs_array)):
            self.dict_scratchcards[int(l)+1] = 1
        print(self.dict_scratchcards)
        return self.dict_scratchcards

    def part2_generate_next_cards(self) -> dict:
        self.scratchcard_sum = 0
        for k, v in enumerate(self.winning_arrays):
            duplicates_len = self._get_duplicates_length(self.winning_arrays[k], self.ans_arrays[k])
            
            #update dict with additional 
            for n in range(1, duplicates_len+1):
                try:
                    self.dict_scratchcards[k+1+n] = self.dict_scratchcards[k+1+n] + self.dict_scratchcards[k+1]*1
                except:
                    pass

            print(f'Names: {k}')
            print(f'----: {duplicates_len}')
            print(f'----: {self.dict_scratchcards}')

        return self.dict_scratchcards

    def part2_calculate_sum(self) -> int:
        self.scratchcard_sum = 0
        for k, v in self.dict_scratchcards.items():
            self.scratchcard_sum += v
        return self.scratchcard_sum

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":
        test_inputs = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        ]
        res_test1 = 13
     
        test_obj = ScratchCards(test_inputs)
        test_obj2 = ScratchCards(test_inputs)

        unittest_dataprocessing = { 
            'test_1': res_test1 == test_obj.run_program("part1"),
            'test_2': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1} == test_obj2.part2_init_dict(),
            'test_3': 30 == test_obj2.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-4-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:
            func_obj = ScratchCards(lines[1])
            sum = func_obj.run_program(mode)
            print(f'Total number is {sum}') 

        else:
            print("Error when opening file!")
        
    