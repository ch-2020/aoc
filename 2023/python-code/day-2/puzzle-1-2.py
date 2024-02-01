import sys, os
import re

sys.path.append("..")
from funcs.readfile import ReadFileObject 

class GameGuessing:
    def __init__(self, max_red, max_green, max_blue):
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue
        self.games_record = {}
        self.total_id = 0
        self.total_sum_power = 0

    def generate_dict(self, lines):
        dp = DataProcessing()
        for l in lines:
            game_id = dp.get_game_id(l)
            game_subgames = dp.get_subgames_info(l)
            self.games_record[game_id] = game_subgames
        return self.games_record
    
    def calculate_sum(self):
        if self.games_record:
            for game_key, game_dict in self.games_record.items():
                game_valid = True

                for subgame_key, subgame_dict in game_dict.items():
                    if (subgame_dict['red'] > self.max_red or
                        subgame_dict['green'] > self.max_green or
                        subgame_dict['blue'] > self.max_blue):
                        game_valid = False
                if game_valid:
                    self.total_id += game_key
                    print(f'-----Valid game {game_key} - Current total: {self.total_id}------')
        return self.total_id

    def generate_maxcolor_from_dict(self):
        if self.games_record:
            for game_key, game_dict in self.games_record.items():
                max_red_seen = 0
                max_green_seen = 0
                max_blue_seen = 0

                for subgame_key, subgame_dict in game_dict.items():
                    if subgame_dict['red'] > max_red_seen: 
                        max_red_seen = subgame_dict['red']
                    if subgame_dict['green'] > max_green_seen:
                        max_green_seen = subgame_dict['green']
                    if subgame_dict['blue'] > max_blue_seen:
                        max_blue_seen = subgame_dict['blue']
                self.games_record[game_key]['min_req_values'] = {
                    'min_req_red': max_red_seen, 
                    'min_req_green': max_green_seen,
                    'min_req_blue': max_blue_seen }
                self.games_record[game_key]['sum_power'] = max_red_seen * max_green_seen * max_blue_seen
                print(f'----- Game {game_key} - min req red/green/blue: {max_red_seen},{max_green_seen},{max_blue_seen} ------')
        return self.games_record
    
    def calculate_sum_power(self):
        if self.games_record:
            for game_key, game_dict in self.games_record.items():
                if self.games_record[game_key]['sum_power']:
                    self.total_sum_power += self.games_record[game_key]['sum_power']
        return self.total_sum_power

class DataProcessing:
    def __init__(self) -> None:
        self.color_keys_dict = {'red','green','blue'}

    def get_game_id(self, line) -> int:
        substring = line.split(':')[0]
        value = int(''.join(filter(str.isdigit, substring)))
        return value
    
    def get_subgames_info(self, line) -> dict:
        dict_res = {}
        subgame_id = 1
        
        substrings = (line.split(':')[1]).split(';')
        for sub in substrings:
            dict_res[subgame_id] = {'red':0, 'green':0, 'blue':0}
            color_configs = sub.split(',')
            for color_str in color_configs:
                color_key = re.findall('|'.join(self.color_keys_dict), color_str)[0]
                color_value = int(''.join(filter(str.isdigit, color_str)))
                dict_res[subgame_id][color_key] = color_value
            subgame_id += 1
        return dict_res

if __name__ == "__main__":
    mode = "part1" #"part2", "test"

    if mode == "test":
        dp = DataProcessing()
        unittest_dataprocessing = { 
            'test_1': 3 == dp.get_game_id("Game 3: 7 red, 4 blue, 13 green; 14 green, 1 blue, 1 red; 1 red, 11 green, 5 blue; 10 green, 3 blue, 3 red; 5 red, 5 blue, 3 green"),
            'test_2': {1:{'red':7, 'blue': 4, 'green': 13},2:{'red':1, 'blue': 1, 'green': 14}} == dp.get_subgames_info("Game 3: 7 red, 4 blue, 13 green; 14 green, 1 blue, 1 red")
        }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-2-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        gg = GameGuessing(12, 13, 14)
        gg.generate_dict(lines[1])

        if mode == "part1": 
            if lines[0]:
                sum = gg.calculate_sum()
                print(f'Sum of games id: {sum}')
            else: 
                print(f'Error when reading file!')

        if mode == "part2":
            if lines[0]:
                gg.generate_maxcolor_from_dict()
                sum_power = gg.calculate_sum_power()
                print(f'Sum of power id: {sum_power}')
            else: 
                print(f'Error when reading file!')

