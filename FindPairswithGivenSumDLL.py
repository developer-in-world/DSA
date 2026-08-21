from DoublyLinkedList import DoublyLinkedList

class Solution:
    def bruteForce(self, head, target):
        if head is None or head.next is None:
            return []
                
        temp1 = head
        result = []
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.value + temp2.value == target:
                    result.append([temp1.value, temp2.value])
                temp2 = temp2.next
            temp1 = temp1.next
        
        return result
    
    def betterSolution(self, head, target):
        if head is None or head.next is None:
            return []
        
        temp = head
        my_set = set()
        result = []
        
        while temp is not None:
            remaining = target - temp.value
            if remaining in my_set:
                result.append([remaining, temp.value])
            my_set.add(temp.value)
            temp = temp.next
        
        return result
    
    def optimalSolution(self, head, target):
        if head is None or head.next is None:
            return []
        
        result = []
        right = head
        while right.next is not None:
            right = right.next
        left = head
        
        while left is not None and right is not None and left.value < right.value:
            if left.value + right.value == target:
                result.append([left.value, right.value])
                left = left.next
                right = right.prev
            elif left.value + right.value > target:
                right = right.prev
            else:
                left = left.next
        
        return result
        
             
            



nums = list(map(int, input().split()))
target = int(input())
dd = DoublyLinkedList()
head = dd.create_doubly_linked_list(nums)
solver = Solution()
result = solver.optimalSolution(head, target)
print(result)

