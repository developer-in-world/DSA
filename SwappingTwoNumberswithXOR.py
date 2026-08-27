def swapTwoNumbers(num1, num2):
    num1 = num1^num2
    num2 = num1^num2
    num1 = num1^num2
    
    print(f"This is num1: {num1}")
    print(f"This is num2: {num2}")
    
swapTwoNumbers(22, 10)