import uuid

class Node:

    nodes = []

    def __init__(self, pos_x, pos_y, type=1):
        self.id = uuid.uuid4()

        self.distance = None
        self.type = 0

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.nodes = []
        Node.nodes.append(self)

    def addNode(self, node):
        self.nodes.append(node)

    def __str__(self):
        return "node uuid: {} x: {} y:{} distance:{}".format(self.id, self.pos_x, self.pos_y, self.distance)

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

