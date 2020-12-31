from __future__ import annotations
from abc import abstractmethod

class INode(object):

    # list of all nodes of the class
	nodes: list[INode] = []

	@staticmethod
	def findbyId(node_id: str) -> INode:
		try:
			return INode.findByFilter(lambda x: x.id == node_id)[0]
		except IndexError as e:
			return None 

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

	def linkNode(self, node: INode):
		if node not in self.nodes:
			self.nodes.append(node)
			node.linkNode(self)

	def accept(self, solver: ISolver):
		solver.resolve(self)

class ISolver(object):

  @abstractmethod
  def resolve(self, node: INode):
    raise NotImplementedError()

  @abstractmethod
  def run(self):
    raise NotImplementedError()

  @abstractmethod
  def step(self):
    raise NotImplementedError()

  @abstractmethod
  def getPath(self):
    raise NotImplementedError()