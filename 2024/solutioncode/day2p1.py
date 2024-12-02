from global_ import globalvariables as gv
f = gv.filecontent

import re

def get_sign(num):
    if num == 0:
        return 0
    else:
        return int(num/abs(num))

def check_condition(num, prev_sign):
    sign_nr = get_sign(num)
    if abs(num) == 0 or abs(num) > 3 or sign_nr is not prev_sign:
        return False
    else:
        return True

sum = 0
for l in f.split("\n"):
    nums = [int(i) for i in re.findall(r'\d+', l)]
    nr_nums = len(nums)

    init_diff = nums[1] - nums[0]
    init_sign = get_sign(init_diff)

    for n, item in enumerate(nums[1:nr_nums]):
        diff = nums[n+1] - nums[n]
        if check_condition(diff, init_sign) == False:
            break
        else:
            init_sign = get_sign(diff)
            if n == nr_nums - 2:
                sum += 1
        
print(sum)
        
