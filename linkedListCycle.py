class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def createHead(nums):
    if len(nums) == 0:
        return None
    else:
        head = Node(nums[0])
        current = head
        for i in range(1,len(nums)):
            current.next = Node(nums[i])
            current = current.next
        return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.value, end="")
        temp = temp.next
    print()
    

class Solution:
    def bruteForce(self, head):
        my_set = set()
        temp = head
        
        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
            
        return False
    
    def optimalSolution(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


nums = list(map(int, input().split()))
head = createHead(nums)
head.next.next = head.next
solver = Solution()
result = solver.optimalSolution(head)
print(result)