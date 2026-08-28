def leftfunc(num, i):
    if (num & (1<<i)) != 0:
        return True
    else: # using the left shift ops
        return False
        
print(leftfunc(13, 1))
print(leftfunc(13, 2))
print(leftfunc(13, 4))

def rightfunc(num, i):
    if ((num>>i) & 1) == 1:
        return True
    else:
        return False

print("\n")
print(rightfunc(13, 1))
print(rightfunc(13, 2))
print(rightfunc(13, 4))