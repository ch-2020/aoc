import numpy as np
import pprint as pp
import re

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, bucket, key, val):
        # 1. Get the bucket of the key
        bucket = self.hash_table[bucket]
        found_key = False
        for i, r in enumerate(bucket):
            rec_key, rec_val = r
            if rec_key == key:
                found_key = True
                break
        
        # 2. If bucket has the same key, update or append
        if found_key:
            bucket[i] = (key, val)
        else:
            bucket.append((key, val))
    
    def get_bucket(self, bucket):
        # 1. Get bucket
        return self.hash_table[bucket]
        
    def delete_val(self, bucket, key):
        # 1. Get bucket
        bucket = self.hash_table[bucket]
        found_key = False
        for i, r in enumerate(bucket):
            rec_key, rec_val = r
            if rec_key == key:
                found_key = True
                break
        
        # 2. return key
        if found_key:
            bucket.pop(i)
        return
    
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

class LensLib:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

        #part2
        self.extracted_key_data = []

    def run_program(self, mode) -> int:
        if mode == "part1":
            self.extract_data()
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.extract_key_data()
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readline().strip()
            self.extracted_data = self.inputs.split(",")
            pp.pprint(self.extracted_data)
    
    def extract_key_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readline().strip()
            self.extracted_data = self.inputs.split(",")
            for data in self.extracted_data:
                self.extracted_key_data.append(tuple(x for x in re.split('([=-])', data)))
            temp = []
            for id, kd in enumerate(self.extracted_key_data):
                v = 0
                for c in [*kd[0]]:
                    v = self.turn(v,c)
                temp.append(kd + (v,))
            self.extracted_key_data = temp
            pp.pprint(self.extracted_key_data)

    def turn(self, value, code) -> int:
        return ((value + ord(code)) * 17)%256

    def cal_part2(self, hash_table: HashTable):
        sum = 0
        for num in range(256):
            for box_num, box in enumerate(hash_table.get_bucket(num)):
                sum += (num+1) * (box_num+1) * int(box[1])
        return sum

    def part1_solution(self) -> int:
        sum = 0
        for hash in self.extracted_data:
            current = 0
            for c in [*hash]:
                current = self.turn(current, c)
            sum += current
        return sum

    def part2_solution(self) -> int:
        hash_table = HashTable(256)
        for d in self.extracted_key_data:
            key, sym, val, buc = d
            if sym == '-':
                hash_table.delete_val(buc, key)
            elif sym == '=':
                hash_table.set_val(buc, key, val)
        return self.cal_part2(hash_table)

if __name__ == "__main__":
    mode = "part2" #"part2", "test"

    if mode == "test":     
        test_obj = LensLib("puzzle-test.txt")
        unittest_dataprocessing = { 
            #'test_1': 1320 == test_obj.run_program("part1"),
            'test_2': 145 == test_obj.run_program("part2")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = LensLib("puzzle-15-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}')