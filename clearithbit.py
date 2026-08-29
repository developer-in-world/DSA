def clearIthBit(num, i):
    return num & ~(1<<i) # optimal, in brute force we would need to convert into binary and check it index and clear bit if it one, We could use the previous set script with slight changes, so I have skipped it here.

print(clearIthBit(13, 2))
print(clearIthBit(13, 3))