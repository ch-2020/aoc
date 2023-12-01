import re 

keywords = {
    '1','2','3','4','5','6','7','8','9',
    'one', 'two', 'three', 'four', 'five', 
    'six', 'seven', 'eight', 'nine'}

reversed_keywords = {
     '1','2','3','4','5','6','7','8','9',
    'eno', 'owt', 'eerht', 'ruof', 'evif', 
    'xis', 'neves', 'thgie', 'enin'
}

dict_keywords = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    'eno' : 1,
    'owt' : 2,
    'eerht' : 3,
    'ruof' : 4,
    'evif' : 5,
    'xis' : 6,
    'neves' : 7,
    'thgie' : 8,
    'enin' : 9,
}

input_lines = []
total_sum = 0
with open("day-1/puzzle-1-input.txt") as file:
    input_lines = file.readlines()

#Edge cases
#input_lines = ['eighthree', 'sevenine']

for l in input_lines:
    first_num = re.findall('|'.join(keywords), l)[0]
    
    rl = l[::-1]
    last_num = re.findall('|'.join(reversed_keywords), rl)[0]

    try: 
        first_num_int = int(first_num)
    except:
        first_num_int = dict_keywords[first_num]
    try: 
        last_num_int = int(last_num)
    except:
        last_num_int = dict_keywords[last_num]
    tmp_res = int(str(first_num_int) + str(last_num_int)) 
    total_sum += tmp_res

print(f'Total sum is {total_sum}') 