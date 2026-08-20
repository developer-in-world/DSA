from DoublyLinkedList import DoublyLinkedList

class Solution:
    def optimalSolution(self, head, key):
        if head.next is None and head.value == key:
            return None
        
        temp = head
        prev = None
        newHead = head
        
        while temp is not None:
            if temp.value == key:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == newHead:
                    newHead = newHead.next
                    
            
            else:
                prev = temp
                
            temp = temp.next
        
        return newHead


dd = DoublyLinkedList()
nums = list(map(int,input().split()))
k = int(input())
head = dd.create_doubly_linked_list(nums)
solver = Solution()
result = solver.optimalSolution(head, k)
dd.head = result
dd.printing_doubly_linked_list()


