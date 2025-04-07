class Node():
    def __init__ (self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "카카로트"
print(node1.data,end = ' ')

    
node2 = Node()
node2.data = "브로리"
node1.link = node2

print(node1.link.data,end = ' ')
