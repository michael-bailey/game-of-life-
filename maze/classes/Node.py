from __future__ import annotations
from abc import abstractmethod
from .interfaces import INode, ISolver

import uuid

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
	yield current

class DijkstraSolver(ISolver):

  def __init__(self) -> None:
      super().__init__()
      print("[ DijkstraSolver ]")
      print("method: init")
      
      self.queue = PriorityQueue()

      self.start: Node = None
      self.end: Node = None

  def resolve(self, node: Node):

    if node.distance == None: node.distance = 0

    for child in node.nodes:
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
      
  def getPath(self) -> list[Node]:
    if self.start != None or self.end != None:
      path: list[Node] = []
      current = self.end
      while current.previous != None:
        path.append(current)
        current = Node.findbyId(current.previous)
      path.append(current)
      return path
