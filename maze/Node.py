import uuid

class Node:

    nodes = []

    def __init__(self, pos_x, pos_y, type=1):
        print()

        self.id = uuid.uuid4()
        self.type = 0

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.top = None
        self.left = None
        self.right = None
        self.bottom = None

        print(self)

        Node.nodes.append(self)

    def setLeft(self, node):
        self.left = node
        
    def setRight(self, node):
        self.right = node
        
    def setTop(self, node):
        self.top = node
        
    def setBotton(self, node):
        self.bottom = node

    def __str__(self):
        return "node uuid: {} x: {} y:{}".format(self.id, self.pos_x, self.pos_y)
        