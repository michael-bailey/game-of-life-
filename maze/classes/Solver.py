from .Node import INode, Node

class ISolver(object):

  def resolve(self, node_id: INode):
    raise NotImplementedError

  def run(self):
    raise NotImplementedError