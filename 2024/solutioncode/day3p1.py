from global_ import globalvariables as gv
f = gv.filecontent

extracted_muls = []
current_char = 0
max_len = 0

input = "".join(f.split("\n"))
max_len = len(input)
current_index = input.find("mul(")
extracted_muls.append(input[current_index:current_index+12])

print(f'max_len: {max_len}, extracted_muls: {extracted_muls}')

#keep looping to find the next 'mul('
while current_char < max_len:
    #check the next hit
    #if not found, current_char == max_len
    pass