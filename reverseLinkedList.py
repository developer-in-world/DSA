class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def createLL(nums):
    if len(nums) == 0:
        return None
    
    head = Node(nums[0])
    current = head
    
    for i in range(1, len(nums)):
        current.next = Node(nums[i])
        current = current.next
    
    return head

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.value, end=" ")
        temp = temp.next
    print()
    
class Solution:
    def bruteForce(self, head):
        temp = head
        stack = []
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
        temp = head
        previous = None
        
        while temp is not None:
            front = temp.next
            temp.next = previous
            previous = temp
            temp = front
        
        return previous


nums = list(map(int, input().split()))
head = createLL(nums)
solver = Solution()
result = solver.optimalSolution(head)
printLL(result)