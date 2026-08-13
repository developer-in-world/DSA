from LinkedListStructureandBasicCodes import Node, createLinkedList, printLinkedList


class Solution:
    def myVersion(self, head):
        my_list = list()
        temp = head
        
        # I have some errors in the code handling of edge cases , but I am improving my self
        if head is None or head.next is None:
            return head
        
        while temp is not None and temp.next is not None:
            my_list.append(temp.value)
            temp = temp.next.next
        
        my_list.append(temp.value)
        
        temp = head.next
        while temp is not None and temp.next is not None:
            my_list.append(temp.value)
            temp = temp.next.next
        
        temp = head
        index = 0
        
        while temp is not None:
            temp.value = my_list[index]
            index += 1
            temp = temp.next
        
        return head
    
    
    def bruteForce(self, head):
        temp = head
        space = list()
        # This version of the code is much cleaner and readable by you guys , so I am improving myself 
        if head is None or head.next is None:
            return head
        
        while temp is not None:
            space.append(temp.value)
            if temp.next is None:
                break
            temp = temp.next.next
        
        temp = head.next

        while temp is not None:
            space.append(temp.value)
            if temp.next is None:
                break
            temp = temp.next.next
        
        temp = head
        index = 0

        while temp is not None:
            temp.value = space[index]
            index += 1
            temp = temp.next
        
        return head
    
    def optimalSolution(self, head):
        
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = even_head
        return head
        
        
        
        
            
            

solver = Solution()
nums = list(map(int, input().split()))
head = createLinkedList(nums)
result = solver.optimalSolution(head)
printLinkedList(result)