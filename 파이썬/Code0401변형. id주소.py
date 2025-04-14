class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

print(node2.data)

print(id(node1.link))
print(id(node2))
