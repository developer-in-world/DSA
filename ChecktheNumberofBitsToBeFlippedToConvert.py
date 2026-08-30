def numberOfBitsToBeFlipped(start, goal):
    ans = start ^ goal
    count = 0
    for i in range(0, 32):
        if ans & (1<<i) != 0:
            count += 1
    
    return count


print(numberOfBitsToBeFlipped(-10, 10))
print(numberOfBitsToBeFlipped(10, 7))
print(numberOfBitsToBeFlipped(3, 4))