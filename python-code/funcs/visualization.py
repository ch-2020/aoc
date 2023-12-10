import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt 
import time 

data = {'C':20, 'C++':15, 'Java':30, 
        'Python':35}
courses = list(data.keys())
values = list(data.values())

plt.ion()
fig = plt.figure()

plt.bar(courses, values, color ='gray', width = 0.1)
plt.xticks([])

for x in range(50):
    values = [n+x for n in values]
    print(values)
    plt.bar(courses, values, color ='blue', width = 0.1)
    plt.xticks([])
    fig.canvas.draw()
    plt.pause(0.5)


input()


