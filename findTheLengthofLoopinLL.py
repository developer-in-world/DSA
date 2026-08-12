from LinkedListStructureandBasicCodes import Node, createLinkedList, printLinkedList


class Solution:
    def bruteForce(self, head):
        travel = 0
        my_dict = {}
        temp = head
        
        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0
    
    def optimalSolution(self, head):
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
                


solver = Solution()
nums = list(map(int, input().split()))
head = createLinkedList(nums)
head.next.next.next = head
result = solver.optimalSolution(head)
print(result)
