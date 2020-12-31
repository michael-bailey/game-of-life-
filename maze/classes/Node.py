from __future__ import annotations
from abc import abstractmethod
from maze.classes.Solver import ISolver

import uuid

class INode(object):

    # list of all nodes of the class
	nodes: list[INode] = []

	@staticmethod
	def findbyId(node_id: str) -> list[INode]:
		return INode.findByFilter(lambda x: x.id == node_id)

	@staticmethod
	def findbyPos(x: int, y: int) -> list[INode]:
		return INode.findByFilter(lambda x: x.pos_x == x and x.pos_y == y)

	@staticmethod
	def findbyArea(x1: int, y1: int, x2: int, y2: int) -> list[INode]:
		return INode.findByFilter(lambda x: x.pos_x == x1 and x.pos_y == y1 and x.pos_x == x2 and x.pos_y == y2)

	@staticmethod	
	def findByFilter(fn) -> list[INode]:
		return [x for x in INode.nodes if fn(x) == True]

	@staticmethod
	def addNode(node: INode):
		INode.nodes.append(node)

	@abstractmethod
	def getNodes(self) -> list[INode]:
		raise NotImplementedError()

	def accept(self, solver: ISolver):
		solver.resolve(self)

class Node(INode):

	def __init__(self, pos_x, pos_y, type=1):
		self.id = uuid.uuid4()

		self.distance = None
		self.type = 0

		self.pos_x = pos_x
		self.pos_y = pos_y

		self.previous = None

		self.nodes = []
		Node.nodes.append(self)

	def pathFind(self, recursive = True):
		if recursive:
			if self.previous == None: return [self]
			return self.previous.pathFind(recursive=True) + [self]
        
		nodebacktrack = []
		for i in backtrack(self):
			nodebacktrack.append(i)

		return nodebacktrack


	def __str__(self):
		return "node uuid: {} x: {} y:{} distance:{}".format(self.id, self.pos_x, self.pos_y, self.distance)

	def __lt__(self, other):
		return self.distance < other.distance

	def __gt__(self, other):
		return self.distance > other.distance

def backtrack(node):
	current = node
	while current.previous != None:
		yield current
		current = current.previous
