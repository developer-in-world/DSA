def checkNumberIsPowerOf2(num):
    if num & (num-1) == 0:
        return True
    else:
        return False


print(checkNumberIsPowerOf2(12))
print(checkNumberIsPowerOf2(2))
print(checkNumberIsPowerOf2(13))
print(checkNumberIsPowerOf2(31))
print(checkNumberIsPowerOf2(32))