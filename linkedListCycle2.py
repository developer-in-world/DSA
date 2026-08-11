from LinkedListStructureandBasicCodes import Node, createLinkedList, printLinkedList

class Solution:
    def bruteForce(self, head):
        temp = head
        my_set = set()
        
        while temp is not None:
            if temp in my_set:
                return temp
            my_set.add(temp)
            temp = temp.next
        return None
    
    def optimalSolution(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

nums = list(map(int, input().split()))
head = createLinkedList(nums)
head.next.next = head
solver = Solution()
result = solver.optimalSolution(head)
print(result.value)