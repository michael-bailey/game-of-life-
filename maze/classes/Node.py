import uuid

class Node:

    nodes = []

    def __init__(self, pos_x, pos_y, type=1):
        self.id = uuid.uuid4()

        self.distance = None
        self.type = 0

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.previous = None

        self.nodes = []
        Node.nodes.append(self)

    def addNode(self, node):
        self.nodes.append(node)

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
