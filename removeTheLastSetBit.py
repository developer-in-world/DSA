def removeLastSetBit(num):
    return num & (num-1)


print(removeLastSetBit(16))
print(removeLastSetBit(84))
print(removeLastSetBit(40))