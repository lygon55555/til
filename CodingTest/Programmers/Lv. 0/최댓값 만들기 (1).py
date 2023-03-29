def solution(numbers):
    num1 = 0
    num2 = 0
    
    num1 = max(numbers)
    numbers.remove(num1)
    
    num2 = max(numbers)
    
    return num1*num2