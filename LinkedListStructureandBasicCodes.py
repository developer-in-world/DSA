class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def createLinkedList(nums):
    if len(nums) == 0:
        return None
    else:
        head = Node(nums[0])
        temp = head
        for i in range(1, len(nums)):
            temp.next = Node(nums[i])
            temp = temp.next
        return head

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.value, end=" ")
        temp = temp.next
    print()