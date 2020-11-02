from numpy.core.records import array
from .Node import Node
from PIL.Image import Image, open as openImage, fromarray
import PIL
import numpy as np
from pprint import pprint
from queue import PriorityQueue

PIL.Image.MAX_IMAGE_PIXELS = 933120000

class Maze(object):
    
    def __init__(self, filename, output_image=False, verbose=False, threads=1):

        self.verbose = verbose

        # open the image file
        self.image = openImage(filename)

        # turn image file into an array
        self.mazeArray = np.asarray(self.image)

        # create empty node array for the nodes
        self.nodeMap = [[None for _ in range(self.image.width)] for _ in range(self.image.height)]

        # verbose option
        if verbose: print(self.nodeMap)

        # TODO: - thread this part
        # create start node and fetch id
        for i in range(len(self.mazeArray[0])):
            if self.mazeArray[0][i] == True:
                self.startNode = Node(i, 0)
                self.nodeMap[0][i] = self.startNode
                break
        
        # TODO: - thread this part
        # create end node and get id
        for i in range(len(self.mazeArray[len(self.mazeArray)-1])):
            if  self.mazeArray[len(self.mazeArray)-1][i] == True:
                self.endNode = Node(i, len(self.mazeArray)-1)
                self.nodeMap[len(self.mazeArray)-1][i] = self.endNode
                break

        # TODO: - thread this part
        # generate nodes for each corner or juntion for the maze
        for y in range(1, len(self.mazeArray)-1):
            for x in range(1, len(self.mazeArray[0])-1):
                if verbose: print("---| x:{} y:{} |---".format(x, y))
                createNode = self.isNode(x, y)
                if verbose: print("is node? ", createNode)
                if createNode:
                    self.nodeMap[y][x] = Node(x, y)

        # if the output image is set then generate node image for the graph
        if output_image:
            nodeImageArray = np.full((self.image.width, self.image.height), False, dtype=bool)

            for y in range(len(self.nodeMap)):
                for x in range(len(self.nodeMap[y])):
                    if self.nodeMap[y][x] != None:
                        nodeImageArray[y][x] = True

            fromarray(nodeImageArray).save("./nodes.png")

        if output_image: self.pathsImage = np.full((self.image.width, self.image.height), False, dtype=bool)

        # scan over all rows and create left to right connections
        if verbose: print(" ---| linking rows |---")
        for y in range(len(self.mazeArray)):
            currentNode = None
            for x in range(len(self.mazeArray[0])):

                # if on wall clear the current node
                if verbose: print("path: ", self.mazeArray[y][x])
                if not self.mazeArray[y][x]:
                    currentNode = None
                    continue

                # if none skip this node
                if verbose: print("node: ", self.nodeMap[y][x])
                if self.nodeMap[y][x] == None:
                    if output_image: self.pathsImage[y][x] = True
                    continue

                if verbose: print("current node: ", currentNode)
                if currentNode == None:
                    currentNode = self.nodeMap[y][x]
                    if output_image: self.pathsImage[y][x] = True
                    continue

                if verbose: print("created link: ", currentNode, " => ", self.nodeMap[y][x])
                if currentNode != None:
                    currentNode.addNode(self.nodeMap[y][x])
                    self.nodeMap[y][x].addNode(currentNode)
                    currentNode = self.nodeMap[y][x]
                    if output_image: self.pathsImage[y][x] = True

        # scan all columns and create all top to bottom connections
        if verbose: print(" ---| linking columns |---")
        for x in range(len(self.mazeArray[0])):
            currentNode = None
            for y in range(len(self.mazeArray)):
            
                # if on wall clear the current node
                if verbose: print("path: ", self.mazeArray[y][x])
                if not self.mazeArray[y][x]:
                    currentNode = None
                    continue

                # if none skip this node
                if verbose: print("node: ", self.nodeMap[y][x])
                if self.nodeMap[y][x] == None:
                    if output_image: self.pathsImage[y][x] = True
                    continue

                if verbose: print("current node: ", currentNode)
                if currentNode == None:
                    currentNode = self.nodeMap[y][x]
                    if output_image: self.pathsImage[y][x] = True
                    continue

                if verbose: print("created link: ", currentNode, " => ", self.nodeMap[y][x])
                self.nodeMap[y][x].addNode(currentNode)
                currentNode.addNode(self.nodeMap[y][x])

                currentNode = self.nodeMap[y][x]
                if output_image: self.pathsImage[y][x] = True       



        if output_image:
            fromarray(self.pathsImage).save("paths.png")



    def isNode(self, x, y):

        if self.verbose: print("\t", self.mazeArray[-1][x-1], "\t", self.mazeArray[y-1][x], "\t", self.mazeArray[y-1][x+1])
        if self.verbose: print("\t", self.mazeArray[y][x-1], "\t", self.mazeArray[y][x], "\t", self.mazeArray[y][x+1])
        if self.verbose: print("\t", self.mazeArray[y+1][x-1], "\t", self.mazeArray[y+1][x], "\t", self.mazeArray[y+1][x+1])

        if not self.mazeArray[y][x]:
            return False
        
        if self.mazeArray[y+1][x] and self.mazeArray[y][x+1]:
            return True

        if self.mazeArray[y+1][x] and self.mazeArray[y][x-1]:
            return True

        if self.mazeArray[y-1][x] and self.mazeArray[y][x+1]:
            return True

        if self.mazeArray[y-1][x] and self.mazeArray[y][x-1]:
            return True

        return False

    def solve_dikstra(self):
            print(" ---| initalising |--- ")
            queue = PriorityQueue()
            doneList = []
            distance = 0
            nodeList = []

            if self.verbose: print(" ---| adding start node |--- ")
            self.startNode.distance = 0
            queue.put(self.startNode)

            # while there are items in the queue
            while not queue.empty():

                # get the next item
                current = queue.get()
                if self.verbose: print("node: ", current)

                # for each node update distance
                for node in current.nodes:
                    diff = abs(current.pos_x - node.pos_x) if abs(current.pos_x - node.pos_x) > 0 else abs(current.pos_y - node.pos_y)

                    if self.verbose: print("diff: ", diff)
                    if node.distance == None or node.distance > current.distance + diff:
                        node.distance = current.distance + diff
                        queue.put(node)

                doneList.append(current)

                    
            print(" ---| route |---")
            for i in doneList:
                if i is self.startNode: print("start: ", i)
                elif i is self.endNode: print("end: ", i)
                else: print("node: ", i)
                if i is self.endNode:
                    break

