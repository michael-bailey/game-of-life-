from __future__ import annotations

import faulthandler as fh
import gc
from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint
from queue import PriorityQueue
from sys import path
from time import time

import numpy as np
import PIL
from numpy.core.records import array
from PIL.Image import Image, fromarray
from PIL.Image import open as openImage

from .interfaces import ISolver
from .Node import Node

PIL.Image.MAX_IMAGE_PIXELS = 933120000
fh.enable()

class Maze(object):

	@staticmethod
	def mazeFromImageFile(filename: str) -> Maze:
		pass

	@staticmethod
	def mazeFomeImage() -> Maze:
		pass


	def __init__(self, filename, output_image=False, verbose=False, threaded=True):
		self.verbose = verbose
		print("[ info ]")

		# open the image file
		self.image = openImage(filename)
		self.width = self.image.width
		self.height = self.image.height

		print("width:\t", self.width)
		print("height:\t", self.height)

		# turn image file into an array
		self.mazeArray = np.asarray(self.image)

		# create empty node array for the nodes
		nodeMap = [[None for _ in range(self.width)] for _ in range(self.height)]

		# TODO: - thread this part
		# create start node and fetch id
		for i in range(len(self.mazeArray[0])):
			if self.mazeArray[0][i] == True:
				self.startNode = Node(i, 0)
				nodeMap[0][i] = self.startNode
				break

		# create end node and get id
		for i in range(len(self.mazeArray[len(self.mazeArray)-1])):
			if  self.mazeArray[len(self.mazeArray)-1][i] == True:
				self.endNode = Node(i, len(self.mazeArray)-1)
				nodeMap[len(self.mazeArray)-1][i] = self.endNode
				break


		startTime = time()
		self._genNodes(nodeMap=nodeMap, verbose=verbose) if not threaded else self._genNodesThreaded(nodeMap=nodeMap, verbose=verbose)
		endTime = time()
		print("time:\t", endTime - startTime)
		print("nodes:\t", len(Node.nodes))

		# if the output image is set then generate node image for the graph
		if output_image:
			nodeImageArray = np.full((self.width, self.height), False, dtype=bool)
			for y in range(len(nodeMap)):
				for x in range(len(nodeMap[y])):
					if nodeMap[y][x] != None:
						nodeImageArray[y][x] = True

						fromarray(nodeImageArray).save("./nodeMap.png")

		if output_image: self.pathsImage = np.full((self.width, self.height), False, dtype=bool)

		# scan over all rows and create left to right connections
		if verbose: print("[ Linking rows]")
		for y in range(len(self.mazeArray)):
			currentNode = None
			for x in range(len(self.mazeArray[0])):

				if verbose: print("[ tile x: {}, y: {} ]".format(x, y))

				# if on wall clear the current node
				if verbose: print("is path: ", self.mazeArray[y][x])
				if not self.mazeArray[y][x]:
					currentNode = None
					continue

				# if none skip this tile
				if verbose: print("has node: ", nodeMap[y][x])
				if nodeMap[y][x] == None:
					if output_image: self.pathsImage[y][x] = True
					continue

				# if it is a node set current node
				if verbose: print("current node: ", currentNode)
				if currentNode == None:
					currentNode = nodeMap[y][x]
					if output_image: self.pathsImage[y][x] = True
					continue

				# if there is a current node link it
				if verbose: print("created link: ", currentNode, " => ", nodeMap[y][x])
				if currentNode != None:
					currentNode.linkNode(nodeMap[y][x])
					#nodeMap[y][x].addNode(currentNode)
					currentNode = nodeMap[y][x]
					if output_image: self.pathsImage[y][x] = True



		# scan all columns and create all top to bottom connections
		if verbose: print("[ Linking columns]")
		for x in range(len(self.mazeArray[0])):
			currentNode = None
			for y in range(len(self.mazeArray)):

				if verbose: print("[ tile x: {}, y: {} ]".format(x, y))

				# if on wall clear the current node
				if verbose: print("path: ", self.mazeArray[y][x])
				if not self.mazeArray[y][x]:
					currentNode = None
					continue

				# if none skip this node
				if verbose: print("node: ", nodeMap[y][x])
				if nodeMap[y][x] == None:
					if output_image: self.pathsImage[y][x] = True
					continue

				# if current node is none set current node
				if verbose: print("current node: ", currentNode)
				if currentNode == None:
					currentNode = nodeMap[y][x]
					if output_image: self.pathsImage[y][x] = True
					continue

				if verbose: print("created link: ", currentNode, " => ", nodeMap[y][x])
				if currentNode != None:
					currentNode.linkNode(nodeMap[y][x])
					#nodeMap[y][x].addNode(currentNode)
					currentNode = nodeMap[y][x]
					if output_image: self.pathsImage[y][x] = True


				nodeMap[y][x].addNode(currentNode)
				currentNode.addNode(nodeMap[y][x])

				currentNode = nodeMap[y][x]
				if output_image: self.pathsImage[y][x] = True

		print("[ running gc ]")
		del nodeMap
		result = gc.collect()
		print("result:\t", result)

		if output_image:
			fromarray(self.pathsImage).save("PathMap.png")

	def _genNodes(self, nodeMap, verbose=False):
		for y in range(1, len(self.mazeArray)-1):
			for x in range(1, len(self.mazeArray[0])-1):
				if verbose: print("---| x:{} y:{} |---".format(x, y))
				createNode = self.isNode(x, y)
				if verbose: print("is node? ", createNode)
				if createNode:
					nodeMap[y][x] = Node(x, y)

	def _genNodesThreaded(self, nodeMap, verbose=False):
		with ThreadPoolExecutor() as pool:

			def processRow(y):
				for x in range(1, len(self.mazeArray[0])-1):
					if verbose: print("---| x:{} y:{} |---".format(x, y))
					createNode = self.isNode(x, y)
					if verbose: print("is node? ", createNode)
					if createNode:
						nodeMap[y][x] = Node(x, y)

			futures = []
			for y in range(1, len(self.mazeArray)-1):
				futures.append(pool.submit(processRow, y))

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

	def solve_dikstra(self, recursive = True):
		if self.verbose: print(" ---| initalising |--- ")
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
					node.previous = current
					queue.put(node)

			doneList.append(current)


		print(" ---| route |---")
		img = self.image.convert("RGB")
		solutionArray = img.load()

		pathArray = self.endNode.pathFind(recursive=recursive)

		for i in pathArray:
			if i is self.startNode: print("start: ", i)
			elif i is self.endNode: print("end: ", i)
			else: print("node: ", i)

		for i in range(len(pathArray)-1):
			px = (200, 0, 0)

			a = pathArray[i]
			b = pathArray[i+1]

			# Blue - red
			r = int((i / len(pathArray)) * 255)
			px = (r, 255 - r, 255 - r)

			if a.pos_y == b.pos_y:
				# Ys equal - horizontal line
				for x in range(min(a.pos_x,b.pos_x), max(a.pos_x,b.pos_x)):
					solutionArray[x,a.pos_y] = px
			elif a.pos_x == b.pos_x:
				# Xs equal - vertical line
				for y in range(min(a.pos_y,b.pos_y), max(a.pos_y,b.pos_y) + 1):
					solutionArray[a.pos_x,y] = px

		img.save("solution.png")

	def solve(self, solver: ISolver) -> list:
		self.startNode.accept(solver)
		solver.run()
		pathArray: list = self.endNode.pathFind()

		for i in pathArray:
			if i is self.startNode: print("start: ", i)
			elif i is self.endNode: print("end: ", i)
			else: print("node: ", i)

		img = self.image.convert("RGB")
		solutionArray = img.load()

		for i in range(len(pathArray)-1):

			a = pathArray[i]
			b = pathArray[i+1]

			# Blue - red
			px = (255, 0, 0)

			if a.pos_y == b.pos_y:
				# Ys equal - horizontal line
				for x in range(min(a.pos_x,b.pos_x), max(a.pos_x,b.pos_x)):
					solutionArray[x,a.pos_y] = px
			elif a.pos_x == b.pos_x:
				# Xs equal - vertical line
				for y in range(min(a.pos_y,b.pos_y), max(a.pos_y,b.pos_y) + 1):
					solutionArray[a.pos_x,y] = px

		img.save("solution.png")
