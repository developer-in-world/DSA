from DoublyLinkedList import DoublyLinkedList

dd = DoublyLinkedList()
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


class Solution:
    def fowardNBackward(self, head, next_steps, prev_steps):
        if next_steps < 0 or prev_steps < 0:
            return print("Invalid Inputs")
        else:
            temp = head
            next_count = 1
            while temp.next and next_count < next_steps:
                next_count += 1
                temp = temp.next
            
            prev_count = 1
            while temp.prev and prev_count < prev_steps:
                prev_count += 1
                temp = temp.prev
            
            print(temp.value)



head = dd.create_doubly_linked_list(nums)
solver = Solution()
solver.fowardNBackward(head,14,11)

