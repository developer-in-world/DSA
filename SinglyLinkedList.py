class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end = " ")
                current = current.next
    
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = None
            current_node = self.head
            count = 0
            
            while current_node is not None and count < position:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            previous_node.next = new_node
            new_node.next = current_node

    def delete(self, value):
        current = self.head
        if current.next is not None:
            if current.value == value:
                self.head = current.next
                current.next = None
                del current
                return
            else:
                found = False # this will used to check the value exist in the list or not 
                previous = None
                while current is not None:
                    if current.value == value:
                        found = True
                        break
                    previous = current
                    current = current.next
                if found:
                    previous.next = current.next
                    current.next = None
                    del current
                    return
                else:
                    print("Node not found")
                

    