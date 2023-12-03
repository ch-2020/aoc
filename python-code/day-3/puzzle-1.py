import sys, os
import re

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class SchematicChecker:
    def __init__(self, input_array) -> None:
        self.input_array = input_array
        self.dict_spec_character = {}
        self.dict_all_numbers = {}
        self.total_number = 0

    def run_all(self) -> int:
        self.extract_special_characters()
        self.extract_all_numbers()
        return self.find_sum()

    def extract_special_characters(self) -> dict:
        special_characters = "!@#$%&*()-+?_=/"

        for row_count, item in enumerate(self.input_array):
            self.dict_spec_character[row_count] = {}
            for char_count, char in enumerate(item):
                if char in special_characters:
                    self.dict_spec_character[row_count][char_count] = char
                else:
                    self.dict_spec_character[row_count][char_count] = 'X'
        
        return self.dict_spec_character

    def extract_all_numbers(self) -> dict:
        for row_count, item in enumerate(self.input_array):
            self.dict_all_numbers[row_count] = {}
            all_nums = re.findall('\d+', item)
            
            index = 0
            for n in all_nums:
                index = item.find(str(n), index)
                self.dict_all_numbers[row_count][index] = int(n)
                index += len(str(n))
            
        return self.dict_all_numbers
 
    def find_sum(self, show = False) -> int:
        if self.dict_all_numbers:
            max_row = len(self.input_array)
            max_column = len(self.input_array[0])

            for row_key, row_dict in self.dict_all_numbers.items():
                for num_key, num_val in row_dict.items():
                    len_of_num = len(str(num_val))
                    valid = False

                    #case: top left
                    if row_key == 0 and num_key == 0:
                        if show: print(f'----case top left {row_key},{num_key}:{num_val}')
                        for i in range(0, len_of_num+1):
                            if self.dict_spec_character[0][i] != 'X' or self.dict_spec_character[1][i] != 'X':
                                valid = True
                                break

                    #case: top row 
                    elif row_key == 0 and num_key != 0:
                        if show: print(f'----case top row {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num+1):
                            if self.dict_spec_character[0][i] != 'X' or self.dict_spec_character[1][i] != 'X':
                                valid = True
                                break

                    #case: top right 
                    elif row_key == 0 and num_key == max_column-1:
                        if show: print(f'----case top right {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num):
                            if self.dict_spec_character[0][i] != 'X' or self.dict_spec_character[1][i]!= 'X':
                                valid = True
                                break

                    #case: bottom left 
                    elif row_key == max_row-1 and num_key == 0:
                        if show: print(f'----case bottom left {row_key},{num_key}:{num_val}')
                        for i in range(0, len_of_num+1):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X':
                                valid = True
                                break

                    #case: bottom row 
                    elif row_key == max_row-1 and num_key != 0:
                        if show: print(f'----case bottom row {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num+1):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X':
                                valid = True
                                break

                    #case: bottom right
                    elif row_key == max_row-1 and num_key ==  max_column-1:
                        if show: print(f'----case bottom right {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X':
                                valid = True
                                break

                    #case: rest left 
                    elif num_key == 0:
                        if show: print(f'----case rest left {row_key},{num_key}:{num_val}')
                        for i in range(0, len_of_num+1):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X' or self.dict_spec_character[row_key+1][i] != 'X':
                                valid = True
                                break

                    #case: rest right 
                    elif num_key == max_column-1:
                        if show: print(f'----case rest right {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X' or self.dict_spec_character[row_key+1][i] != 'X':
                                valid = True
                                break
                    
                    #rest 
                    else:
                        if show: print(f'----case rest {row_key},{num_key}:{num_val}')
                        for i in range(num_key-1, num_key+len_of_num+1):
                            if self.dict_spec_character[row_key-1][i] != 'X' or self.dict_spec_character[row_key][i] != 'X' or self.dict_spec_character[row_key+1][i] != 'X':
                                valid = True
                                break

                    if valid:
                        #print(f'valid number is: {num_val}')
                        self.total_number = self.total_number + num_val
                    else:
                        if show: print(f'NOT VALID: {num_val} at {row_key}, {num_key}')

        #if show: print(f'-----{self.dict_spec_character}')
        #if show: print(f'-----{self.dict_all_numbers}')
        print(f'--{self.total_number}--')
        return self.total_number

if __name__ == "__main__":
    mode = "part1" #"part2", "test"

    if mode == "test":
        test_input = [
            "467..114..",
            "...*......",   
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
            ]
        test_input2 = [
            "12.......*..",
            "+.........34",
            ".......-12..",
            "..78........",
            "..*....60...",
            "78.........9",
            ".5.....23..$",
            "8...90*12...",
            "............",
            "2.2......12.",
            ".*.........*",
            "1.1..503+.56"
        ]

        res_test1 = {0: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 1: {0: 'X', 1: 'X', 2: 'X', 3: '*', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 2: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 3: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: '#', 7: 'X', 8: 'X', 9: 'X'}, 4: {0: 'X', 1: 'X', 2: 'X', 3: '*', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 5: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: '+', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 6: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 7: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 8: {0: 'X', 1: 'X', 2: 'X', 3: '$', 4: 'X', 5: '*', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 9: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}}
        res_test2 = {0: {0: 467, 5: 114}, 1: {}, 2: {2: 35, 6: 633}, 3: {}, 4: {0: 617}, 5: {7: 58}, 6: {2: 592}, 7: {6: 755}, 8: {}, 9: {1: 664, 5: 598}} 

        sc = SchematicChecker(test_input)
        sc2 = SchematicChecker(test_input2)
        unittest_dataprocessing = { 
            'test_1': res_test1 == sc.extract_special_characters(),       
            'test_2': res_test2 == sc.extract_all_numbers(),
            'test_3': 4361 == sc.find_sum(),
            'test4': 925 == sc2.run_all()
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-3-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:
            sc = SchematicChecker(lines[1])
            if mode == "part1": 
                dict_char = sc.extract_special_characters()
                dict_num = sc.extract_all_numbers()
                sum = sc.find_sum(show=False)
                
                print(f'Total number is {sum}')

            if mode == "part2":
                pass 
        else:
            print("Error when opening file!")
        
    