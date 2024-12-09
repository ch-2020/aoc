from global_ import globalvariables as gv
f = gv.filecontent

import re

def is_valid_substring(substring):
    # Define the regex pattern to match "mul(a,b)" with no spaces in brackets
    pattern = r"mul\((\d+),(\d+)\)"
    match = re.search(pattern, substring)
    if match:
        num1, num2 = map(int, match.groups())
        end_index = match.end() - 1
        return True, (num1, num2), end_index
    else:
        return False, None, None

data = "".join(f.split("\n"))
max_len = len(data)

current_index = 0
remaining_data = data
sum = 0

while current_index < max_len:
    #check the next hit
    current_index = remaining_data.find("mul(")
    if current_index == -1:
        current_index = max_len
    else:
        temp_extracted = remaining_data[current_index:current_index+12]
        valid, result, end_index = is_valid_substring(temp_extracted)

        if valid:
            sum += result[0] * result[1]
            remaining_data = remaining_data[current_index+end_index:]
            current_index += current_index + end_index
        else:
            remaining_data = remaining_data[current_index+1:]
            current_index += 1

print(sum)