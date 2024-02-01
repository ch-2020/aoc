input_lines = []
total_sum = 0

with open("day-1/puzzle-day-1-input.txt") as file:
    input_lines = file.readlines()

for l in input_lines:
    tmp_list = [int(c) for c in l if c.isdigit()]
    if tmp_list:
        tmp_res = int(str(tmp_list[0]) + str(tmp_list[len(tmp_list)-1])) 
        total_sum += tmp_res

print(f'Total sum is {total_sum}') 
    

    
