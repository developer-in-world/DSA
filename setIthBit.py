def _intToBinary(num: int) -> str:
    result = ""
    
    while num > 0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"
        
        num = num//2
    
    result = result[::-1]
    return result

def settingIthBitBruteForce(num, i):
    binaryValue = _intToBinary(num)
    index = -(i+1) # python reverse indexing [-3,-2,-1]
    
    if binaryValue[index] == "1":
        return int(binaryValue,2)
    else:
        bList = list(binaryValue)
        bList[index] = "1"
        
        binaryValue = "".join(bList)
        return int(binaryValue,2)

print(settingIthBitBruteForce(9,2))
print(settingIthBitBruteForce(9,0))

def optimalBitwise(num, i):
    return num | (1<<i)

print("\n")
print(optimalBitwise(9,2))
print(optimalBitwise(9,0))