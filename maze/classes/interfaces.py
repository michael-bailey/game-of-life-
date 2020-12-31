from __future__ import annotations
from abc import abstractmethod
from uuid import UUID
import uuid

class INode(object):

    # list of all nodes of the class
	nodes: list[INode] = []
	index: dict[UUID, INode] = {}


	@staticmethod
	def findbyId(node_id: UUID) -> INode:
		return __class__.index[node_id]

	@staticmethod
	def findbyPos(x: int, y: int) -> list[INode]:
		return INode.findByFilter(lambda x: x.pos_x == x and x.pos_y == y)

	@staticmethod
	def findbyArea(x1: int, y1: int, x2: int, y2: int) -> list[INode]:
		return INode.findByFilter(lambda x: x.pos_x == x1 and x.pos_y == y1 and x.pos_x == x2 and x.pos_y == y2)

	@staticmethod	
	def findByFilter(fn) -> list[INode]:
		return [x for x in __class__.nodes if fn(x) == True]

	@staticmethod
	def addNode(node: INode):
		__class__.nodes.append(node)
		__class__.index[node.id] = node


	def __init__(self) -> None:
			super().__init__()

			self.id = uuid.uuid4()
			__class__.addNode(self)

	@abstractmethod
	def getNodes(self) -> list[INode]:
		raise NotImplementedError()

	@abstractmethod
	def linkNode(self, node: INode):
		raise NotImplementedError()

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
  def getPath(self) -> list[INode]:
    raise NotImplementedError()