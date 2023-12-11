import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation

class PipeMaze:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.inputs = []
        self.extracted_data = []

        self.startpoint = ()
        self.start_surronds = []
        self.count = 0
        #shift in row and column
        self.dict_pipes = {
            '|': [(-1, 0), (1, 0)],
            'J': [(-1, 0), (0, -1)],
            'L': [(-1, 0), (0, 1)],
            '-': [(0, -1), (0, 1)],
            'F': [(0, 1), (1, 0)],
            '7': [(0, -1), (1, 0)]
        }

        self.loop_coords = []
        self.plot_data = []
        self.area_count = 0

    def init_plot_demo(self):
        self.rows = len(self.extracted_data)
        self.columns = len(self.extracted_data[0])
        self.plot_data = np.zeros([self.rows, self.columns])
    
    def draw_plot_demo(self):
        self.cmap = colors.ListedColormap(['white','blue'])
        bounds = [0, 0.5, 1]
        self.norm = colors.BoundaryNorm(bounds, self.cmap.N)
        self.fig, self.ax = plt.subplots()
        
        self.ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.1)
        self.ax.set_xticks(np.arange(0, self.columns, 1))
        self.ax.set_yticks(np.arange(0, self.rows, 1))
        self.ax.set(xticklabels=[])  
        self.ax.set(yticklabels=[])  
        self.ax.imshow(self.plot_data, cmap=self.cmap, norm=self.norm)
        plt.savefig('part1_viz.png')

        self.plot_animate = np.zeros([self.rows, self.columns])
        def update(i):
            self.ax.clear()
            point, char = self.loop_coords[i]
            self.plot_animate[point[0]][point[1]] = 1
            self.ax.imshow(self.plot_animate, cmap=self.cmap, norm=self.norm)
            return self.ax
        ani = animation.FuncAnimation(self.fig, update, frames=len(self.loop_coords))
        plt.show()
        ani.save('animation.gif', writer='PillowWriter')
        plt.close() 

    def run_program(self, mode, replace = '') -> int:
        self.extract_data()
        self.init_plot_demo()
        self.find_start()
        if mode == "part1":
            self.sum = self.part1_solution()
            self.draw_plot_demo()
            return self.sum

    def extract_data(self):
        with open(self.filepath, "r") as f:
            self.inputs = f.readlines()
            for l in self.inputs:
                puz = [x for x in [*l.strip()]]
                self.extracted_data.append(puz)

    def find_start(self):
        for p_id, p in enumerate(self.extracted_data):
            for c_id, c in enumerate(p):
                if c == 'S':
                    self.startpoint = (p_id, c_id)
        print(self.startpoint)

    def find_next_item(self, prev_coord, current_coord):
        r = current_coord[0]
        c = current_coord[1]
        symbol = self.extracted_data[r][c]
        shifts = self.dict_pipes[symbol]
        related = [(r + shifts[0][0], c + shifts[0][1]), (r + shifts[1][0], c + shifts[1][1])]
        related.remove(prev_coord)
        return related[0]

    def find_start_surround(self):
        self.start_surronds = []
        left = self.extracted_data[self.startpoint[0]][self.startpoint[1]-1]
        right = self.extracted_data[self.startpoint[0]][self.startpoint[1]+1]
        top = self.extracted_data[self.startpoint[0]-1][self.startpoint[1]]
        bottom = self.extracted_data[self.startpoint[0]+1][self.startpoint[1]]

        if top in ['|', '7', 'F']:
            self.start_surronds.append((self.startpoint[0]-1,self.startpoint[1]))
        if left in ['-', 'F', 'L']:
            self.start_surronds.append((self.startpoint[0],self.startpoint[1]-1))
        if bottom in ['|', 'J', 'L']:
            self.start_surronds.append((self.startpoint[0]+1,self.startpoint[1]))
        if right in ['-', '7', 'J']:
            self.start_surronds.append((self.startpoint[0],self.startpoint[1]+1))

        return self.start_surronds

    def part1_solution(self) -> int:
        surrounds = self.find_start_surround()
        print(f'---- {surrounds} ----')

        self.count = 0
        prev = self.startpoint
        current = surrounds[0]
        self.plot_data[prev[0]][prev[1]] = 3
        self.loop_coords.append((prev, 'S'))

        while current != self.startpoint:
            self.count += 1
            next_step = self.find_next_item(prev, current)
            prev = current
            current = next_step
            self.plot_data[prev[0]][prev[1]] = 1
            self.loop_coords.append((prev, self.extracted_data[prev[0]][prev[1]]))        
        steps = int((self.count + 1) / 2)
        return steps

if __name__ == "__main__":
    mode = "test" #"test"

    if mode == "test":     
        test_obj = PipeMaze("puzzle-test.txt")
        test_obj2 = PipeMaze("puzzle-test2.txt")
        unittest_dataprocessing = { 
            'test_1': 8 == test_obj.run_program("part1")
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        func_obj = PipeMaze("puzzle-day-10-input.txt")      
        sum = func_obj.run_program(mode)    
        print(f'Total number is {sum}')