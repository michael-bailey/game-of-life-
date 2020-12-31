from __future__ import annotations
from abc import abstractmethod
from queue import PriorityQueue
from .interfaces import INode, ISolver

import uuid

class Node(INode):

	def __init__(self, pos_x, pos_y, type=1):
		super().__init__()

		self.distance = None

		self.nodes = []

		self.pos_x = pos_x
		self.pos_y = pos_y

		self.previous = None

	def linkNode(self, node: Node):
		if node not in self.nodes:
			self.nodes.append(node)
			node.linkNode(self)

	def getNodes(self) -> list[Node]:
		return self.nodes

	def pathFind(self, recursive = True):       
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

def backtrack(node: Node):
	print("first: ", node)
	while node.previous != None:
		print("current: ", node)
		yield node
		if not isinstance(node.previous, Node):
			print("next id: ", node.previous)
			node = Node.findbyId(node.previous)
		else:
			print("next node: ", node.previous)
			node = node.previous
	yield node

class DijkstraSolver(ISolver):

	def __init__(self, verbose = False) -> None:
			super().__init__()
			print("[ DijkstraSolver ]")
			print("method: init")

			self.verbose = verbose
			
			self.queue = PriorityQueue()

			self.start: Node = None
			self.end: Node = None

	def resolve(self, node: Node):

		if node.distance == None: node.distance = 0

		for child in node.nodes:
			if not isinstance(child, INode):
				child: Node = Node.findbyId(child)

			diff = abs(child.pos_x - node.pos_x) if abs(child.pos_x - node.pos_x) > 0 else abs(child.pos_y - node.pos_y)
			if self.verbose: print("diff: ", diff)

			if child.distance == None or child.distance > node.distance + diff:
				child.distance = node.distance + diff
				child.previous = node.id
				self.queue.put(child)

	def step(self):
		if not self.queue.empty():
			node: Node = self.queue.get()
			node.accept(self)

	def run(self):
		while not self.queue.empty():
			node: Node = self.queue.get()
			node.accept(self)
			
	def setStart(self, node: Node) -> DijkstraSolver:
		self.start = node
		return self

	def setEnd(self, node: Node) -> DijkstraSolver:
		self.end = node
		return self
	
	def getPath(self) -> list[Node]:
		if self.end != None:
			return self.end.pathFind()
		return None
