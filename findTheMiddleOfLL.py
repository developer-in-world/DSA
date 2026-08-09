class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def createLinkedList(nums):
    if len(nums) == 0:
        return None
    
    head = Node(nums[0])
    current = head
    
    for i in range(1, len(nums)):
        current.next = Node(nums[i])
        current = current.next
    
    return head

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.value, end=" ")
        temp = temp.next
    print()

class Solution:
    def bruteForce(self, head):
        n = 0
        temp = head
        while temp is not None:
            n += 1
            temp = temp.next
        
        temp = head
        for _ in range(0, n//2):
            temp = temp.next
        return temp
    
    def optimalSolution(self, head):
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

nums = list(map(int, input().split()))
head = createLinkedList(nums)
solver = Solution()
result = solver.optimalSolution(head)
printLinkedList(result)
        
