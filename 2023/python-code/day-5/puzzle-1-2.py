import sys, os
import re
import pprint

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class SeedFilter:
    def __init__(self, inputs) -> None:
        self.input_arrays = inputs
        self.map_names_list = [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location"
            ]

        #part1
        self.seed_list = []
        self.maps = {}
        self.extracted_locations = []
        self.min_location = 0

        #part2
        self.seed_list_range = []

    def run_program(self, mode) -> int:
        if mode == "part1":
            self.part1_get_seedlist()
            self.part1_extract_info_from_inputs()
            self.part1_search_map()
            self.part1_findmin()

        elif mode == "part2":
            self.part2_get_seedlist()
            self.part1_extract_info_from_inputs()
            self.part2_search_map()

        return self.min_location

    def part2_get_seedlist(self):
        seedlist_array = self.input_arrays[0].split(":")[1]
        seed_list = [int(x) for x in re.findall('\d+', seedlist_array)]
      
        for i in range(0, len(seed_list), 2):
            self.seed_list_range.append((seed_list[i], seed_list[i] + seed_list[i+1]))

    def part2_search_map(self) -> int:
        if self.maps:
            for k in self.map_names_list:
                new_range = []

                while len(self.seed_list_range) > 0:
                    seed_s, seed_e = self.seed_list_range.pop()

                    for key, value in self.maps[k].items():
                        src_s = value['src']
                        dest_s = value['dest']
                        length = value['len']

                        o_start = max(seed_s, src_s)
                        o_end = min(seed_e, src_s + length)

                        if o_start < o_end:
                            new_range.append((o_start - src_s + dest_s, o_end - src_s + dest_s))
                            if o_start > seed_s:
                                self.seed_list_range.append((seed_s, o_start))
                            if  seed_e > o_end:
                                self.seed_list_range.append((o_end, seed_e))
                            break
                    else:
                        new_range.append((seed_s, seed_e))
                        
                self.seed_list_range = new_range
            
            self.min_location = min(sorted(self.seed_list_range))[0]
        return self.min_location

    def part1_get_seedlist(self):
        seedlist = self.input_arrays[0].split(":")[1]
        self.seed_list = re.findall('\d+', seedlist)

    def part1_extract_info_from_inputs(self):
        #get all maps
        current_map_name = ""
        list_cnt = 0
        for l in range(1, len(self.input_arrays)):
            current_str = self.input_arrays[l]

            if current_str.strip():
                if len(current_str.split(":")) == 2: #new map identified
                    current_map_name = current_str.split(":")[0].split(" ")[0]
                    self.maps[current_map_name] = {}
                    list_cnt = 0

                else: #it is the numbers row
                    self.maps[current_map_name][list_cnt] = {}

                    numberlist =[int(x) for x in current_str.strip().split(" ")]
                    self.maps[current_map_name][list_cnt]["src"] = numberlist[1]
                    self.maps[current_map_name][list_cnt]["dest"] = numberlist[0]
                    self.maps[current_map_name][list_cnt]["len"] = numberlist[2]
                    list_cnt = list_cnt + 1

    def part1_search_map(self):
        self.extracted_locations = []
        if self.maps:
            for seed in self.seed_list:
                temp_val_holder = int(seed)
                for k in self.map_names_list:
                    for key, rules in self.maps[k].items():
                        if temp_val_holder in range(rules['src'], rules['src']+rules['len']+1):
                            temp_val_holder = rules['dest'] + (temp_val_holder - rules['src'])
                            break
                        else: 
                            temp_val_holder = temp_val_holder

                self.extracted_locations.append(temp_val_holder)

    def part1_findmin(self) -> int:
        if self.extracted_locations:
            self.min_location = min(self.extracted_locations)
        return self.min_location

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":
        test_filepath = os.path.join(os.path.dirname(__file__), 'puzzle-test.txt')
        test_lines = ReadFileObject().get_lines_from_file(test_filepath)
    
        test_obj = SeedFilter(test_lines[1])
        unittest_dataprocessing = { 
            'test_1': 35 == test_obj.run_program("part1"),
            'test_2': 46 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-5-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:
            func_obj = SeedFilter(lines[1])
            res = func_obj.run_program(mode)
            print(f'Min location is {res}')

        else:
            print("Error when opening file!")
        
    