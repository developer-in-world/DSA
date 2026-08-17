class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def create_doubly_linked_list(self, nums):
        if len(nums) == 0:
            return None
    
        self.head = Node(nums[0])
        temp = self.head
    
        for i in range(1, len(nums)):
            newNode = Node(nums[i])
            newNode.prev = temp
            temp.next = newNode
            temp = temp.next
            
        return self.head # forgot this line , sorry

    def printing_doubly_linked_list(self):
        if self.head is None:
            return None
    
        temp = self.head
    
        while temp is not None:
            print(temp.value, end=" ")
            last = temp # forward pass
            temp = temp.next
    
        print()
    
        while last is not None:
            print(last.value, end=" ")
            last = last.prev # backward pass
    
        print()
        
    def insert_at_head(self, value):
        newNode = Node(value)
        
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def append(self, value):
        newNode = Node(value)
        
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
    
    def insert_in_between(self, value, position):
        newNode = Node(value)
        
        if position == 0:
            self.insert_at_head(value)
            return
        
        temp = self.head
        index = 0
        
        while temp is not None and index < position-1:
            temp = temp.next
            index += 1
        
        if temp is None:
            print("Index out of Bounds")
            return
        
        newNode.next = temp.next
        newNode.prev = temp
        
        if temp.next:
            temp.next.prev = newNode
        temp.next = newNode
        
    def delete_head(self):
        if not self.head:
            print("Head doesnt exist")
            return
        else:
            newHead = self.head.next
            del self.head
            self.head = newHead
            if self.head:
                self.head.prev = None
            return
        
        
    def delete_last(self):
        if not self.head:
            print("List doesnt exist")
            return

        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            if temp.prev:
                temp.prev.next = None
            else:
                self.head = None

            del temp
            return
        
    def delete_in_between(self, position):
        if not self.head:
            print("List doesnt exist")
            return

        if position == 0:
            self.delete_head()
            return

        temp = self.head
        index = 0

        while temp is not None and index < position:
            temp = temp.next
            index += 1

        if temp is None:
            print("Index out of Bounds")
            return

        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        del temp
        return
    
    '''I think some operations can be done in the TC-->O(1) if I had implemented the tails, here I didnt but we can use it 
    SO feel free to change in your code when youre learning from mine.... Bye Love ya'''
            

    
        
