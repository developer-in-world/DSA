from DoublyLinkedList import DoublyLinkedList

dd = DoublyLinkedList()
nums = list(map(int, input().split()))
head = dd.create_doubly_linked_list(nums)

class Solution:
    def bruteForce(self, head):
        temp = head
        stack = list()
        
        while temp is not None:
            stack.append(temp.value)
            temp = temp.next
        
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.value = e
            temp = temp.next
        
        return head
    
    def optimalSolution(self, head):
        prev = None
        current = head
        
        while current is not None:
            front = current.next
            
            current.next = prev
            current.prev = front
            
            prev = current
            current = front
        
        return prev
            

solver = Solution()
dd.head = solver.optimalSolution(head)
dd.printing_doubly_linked_list()