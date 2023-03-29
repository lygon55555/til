def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            answer = answer + n
        n = n-1
        
    return answer