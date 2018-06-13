import numpy
import sys
import time as t

def insert(array, section, x, y):
    tmpArray = []
    for i in range(len(section)-1):
        for j in range(len(section[i])-1):
            tmpArray[i+x][j+y] = section[i][j]

def fprintarray(array):
    for i in range(len(array)-1):
        for j in range(len(array[i])-1):
            if array[i] [j] == 1:
                sys.stdout.write('█')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
    print()
    print()


start_pos = (10,15)
grid_size = (25,80)

life_form = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]

grid = numpy.zeros(grid_size)
temp = numpy.zeros(grid_size)

fprintarray(insert(grid,life_form,1,1))