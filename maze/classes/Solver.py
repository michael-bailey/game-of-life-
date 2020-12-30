
from .Node import Node


class ISolver(object):


  
  def resolve(self, node_id: INode):
    raise NotImplementedError

  def run(self):
    raise NotImplementedError