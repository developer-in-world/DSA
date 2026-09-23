from collections import deque

lst = deque([]) # empty DLL

lst.append(100)
lst.append(200)
lst.append(300)

print(lst)  # deque([100, 200, 300])


print(lst[0])  # 100 works same like the normal list type methods and indexing in deque

lst.appendleft(1)
lst.appendleft(2)

print(lst)  # deque([2, 1, 100, 200, 300]) inserted at the place of head

print(lst.pop()) # 300 pops the last element 
print(lst.popleft()) # 2 pops the starting elements all are o(1) ops 

"""
There are many sub methods in the deque but for implementing the stack in queue and others we will be using the primary methods like pop, popleft, append, appendleft.

We will learn about other methods in future if required !!!


"""
