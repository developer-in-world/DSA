def convert2Binary(num: int) -> str:
    result = ""
    
    while num > 0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"
        num = num//2
        
    result = result[::-1]
    return result


print(convert2Binary(9))
print(convert2Binary(13))
print(convert2Binary(10))


def convert2Decimal(x: str) -> int:
    decimal_number = 0
    power = 0
    index = len(x) - 1
    
    while index >= 0:
        num = int(x[index]) * (2**power)
        decimal_number += num
        
        index -= 1
        power += 1
    
    return decimal_number

print(convert2Decimal("1101"))