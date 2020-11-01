from numpy.core.records import array
from Node import Node
from PIL.Image import open as openImage, fromarray
import PIL
import numpy as np
from pprint import pprint

PIL.Image.MAX_IMAGE_PIXELS = 933120000

def isNode(array, x, y):

    kernal = array[y-1:y+1,x-1:x+1]
    pprint(kernal)

    print("\t", array[-1][x-1], "\t", array[y-1][x], "\t", array[y-1][x+1])
    print("\t", array[y][x-1], "\t", array[y][x], "\t", array[y][x+1])
    print("\t", array[y+1][x-1], "\t", array[y+1][x], "\t", array[y+1][x+1])

    if not array[y][x]:
        return False
    
    if array[y+1][x] and array[y][x+1]:
        return True

    if array[y+1][x] and array[y][x-1]:
        return True

    if array[y-1][x] and array[y][x+1]:
        return True

    if array[y-1][x] and array[y][x-1]:
        return True

    return False
    

class Maze(object):
    
    def __init__(self, filename, output_node_image=False):
        self.image = openImage(filename)
        
        self.mazeArray = np.asarray(self.image)
        self.nodeMap = [[None for _ in range(self.image.width)] for _ in range(self.image.height)]

        print(self.nodeMap)

        # create start node and fetch id
        for i in range(len(self.mazeArray[0])):
            if self.mazeArray[0][i] == True:
                startNode = Node(i, 0)
                self.nodeMap[0][i] = startNode
                break
        
        # create end node and get id
        for i in range(len(self.mazeArray[len(self.mazeArray)-1])):
            if  self.mazeArray[len(self.mazeArray)-1][i] == True:
                endNode = Node(i, len(self.mazeArray)-1)
                self.nodeMap[len(self.mazeArray)-1][i] = endNode
                break

        # generate graph of the maze ot search
        for y in range(1, len(self.mazeArray)-1):
            for x in range(1, len(self.mazeArray[0])-1):
                print("---| x:{} y:{} |---".format(x, y))
                createNode = isNode(self.mazeArray, x, y)
                print("is node? ", createNode)
                if createNode:
                    self.nodeMap[y][x] = Node(x, y)
        
        nodeImageArray = np.full((self.image.width, self.image.height), False, dtype=bool)

        if output_node_image:
            for y in range(len(self.nodeMap)):
                for x in range(len(self.nodeMap[y])):
                    if self.nodeMap[y][x] != None:
                        nodeImageArray[y][x] = True

            fromarray(nodeImageArray).save("./out.png")

        print(self.nodeMap)