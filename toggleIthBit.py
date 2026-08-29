def toggleIthBit(num, i):
    return num ^ (1<<i)


print(toggleIthBit(13, 2))
print(toggleIthBit(13, 1))
