import numpy as np
import networkx as nx

class Snowverload:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []

    def run_program(self, mode) -> int:       
        if mode == "part1":
            self.sum = self.part1_solution()
            
        elif mode == "part2":
            self.sum = self.part2_solution()
        
        return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            self.extracted_data = {k.strip().split(":")[0]: [] for k in self.inputs}
            for l in self.inputs:
                source = l.strip().split(":")[0]
                dests = l.strip().split(":")[1].split()
                print(source, dests)
                self.extracted_data[source] = dests

    def part1_solution(self) -> int:
        g = nx.Graph()
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                left, right = l.split(":")
                for node in right.strip().split():
                    g.add_edge(left, node)
        
        g.remove_edges_from(nx.minimum_edge_cut(g))
        a, b = nx.connected_components(g)
        sum = len(a) * len(b)
        return sum

    def part2_solution(self) -> int:
        pass

if __name__ == "__main__":
    mode = "part1" # "test"

    if mode == "test":     
        test_obj = Snowverload("puzzle-test.txt")
        unittest_dataprocessing = { 
            'test_1': 54 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = Snowverload("puzzle-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}') #part1: 601344