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

def get_correct(numlist):
    nr_nums = len(numlist)
    init_diff = numlist[1] - numlist[0]
    init_sign = get_sign(init_diff)

    for n, item in enumerate(numlist[1:nr_nums]):
        diff = numlist[n+1] - numlist[n]
        if check_condition(diff, init_sign) == False:  
            return (False, n)
        else:
            init_sign = get_sign(diff)
            if n == nr_nums - 2:
                return (True, 0)

sum = 0
errorlist = []

# Count the correct list
for l in f.split("\n"):
    nums = [int(i) for i in re.findall(r'\d+', l)]
    res, id = get_correct(nums)
    if res == True:
        sum += 1
    else:
        errorlist.append((nums, id))

# redo the error list
updated_list = []
for errlist, ind in errorlist:
    errlist2 = errlist.copy()
    errlist3 = errlist.copy()

    del errlist[ind] # could get correct if first number is removed
    res, id = get_correct(errlist)
    if res == True:
        sum += 1
    else: # could get correct if second number is removed
        del errlist2[ind+1]
        res2, id2 = get_correct(errlist2)
        if res2 == True:
            sum += 1
        else: # edge cases where it could get correct if you remove the first number
            del errlist3[0]
            res3, id3 = get_correct(errlist3)
            if res3 == True:
                sum += 1

print(sum)
