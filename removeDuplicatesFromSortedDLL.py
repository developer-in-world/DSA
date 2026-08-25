from DoublyLinkedList import DoublyLinkedList

class Solution:
    def bruteForce(self, head):
        temp = head # used the SLL concept for finding the loop in the Sll
        if head is None or head.next is None:
            return head
        
        my_set = set()
        while temp is not None:
            if temp.value in my_set:
                temp.prev.next = temp.next
                temp.next.prev =  temp.prev
            my_set.add(temp.value)
            temp = temp.next
        
        return head # TC -> O(N), SC -> O(N)
    
    def optimalSolution(self, head):
        curr = head
        if head is None or head.next is None:
            return head
        
        while curr is not None:
            if curr.prev and curr.prev.value == curr.value:
                if curr.prev == head:
                    curr.prev = None
                    head = curr
                else:
                    curr.prev.prev.next = curr
                    curr.prev = curr.prev.prev
            curr = curr.next
        return head


dd = DoublyLinkedList()
nums = list(map(int, input().split()))
head = dd.create_doubly_linked_list(nums)
solver = Solution()
dd.head = solver.optimalSolution(head)
dd.printing_doubly_linked_list()