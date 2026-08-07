class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#print(f"Printing the object gives its address to us: {node1}")
print(f"We use the attributes to print the value and next address of the node, value = {node1.value} and next add = {node1.next}")
print(f"Printing the last node value, we can print like this also last node value = {node1.next.next.next.next.value}")