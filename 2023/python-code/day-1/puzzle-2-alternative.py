#Online resources
import re

input_lines = []
total_sum = 0

with open("./puzzle-1-input.txt") as file:
    input_lines = file.readlines()

for l in input_lines:
    r = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'

    x = [*map({n: str(i%9+1) for i, n in enumerate(r.split('|'))}.get,
        re.findall(rf'(?=({r}))', l))]
    tmp_res = int(str(x[0]) + str(x[len(x)-1])) 
    total_sum += tmp_res

print(total_sum)