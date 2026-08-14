from LinkedListStructureandBasicCodes import Node, createLinkedList, printLinkedList

class Solution:
    def bruteForce(self, head, n):
        length = 0
        temp = head
        
        while temp is not None:
            length += 1
            temp = temp.next
        
        if length == n:
            new_head = head.next
            del head
            return new_head
        
        pos_to_stop = length - n
        temp = head
        count = 1
        while count < pos_to_stop:
            count += 1
            temp = temp.next
        
        garbage = temp.next
        temp.next = temp.next.next
        del garbage
        return head
    
    def optimalSolution(self, head, n):
        slow = head
        fast = head
        
        for _ in range(n):
            fast = fast.next
        
        if fast == None:
            newhead = head.next
            del head
            return newhead
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        garbage = slow.next
        slow.next = slow.next.next
        del garbage
        return head
        
        
        
        
        
        

solver = Solution()
nums = list(map(int, input("Enter the array values: ").split()))
n = int(input("Enter the N: "))
head = createLinkedList(nums)
result = solver.optimalSolution(head, n)
printLinkedList(result)

