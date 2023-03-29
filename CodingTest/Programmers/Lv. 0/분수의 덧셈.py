def solution(numer1, denom1, numer2, denom2):
    answer0 = 0
    answer1 = 0
    
    answer0 = numer1*denom2 + numer2*denom1
    answer1 = denom1*denom2
    
    for i in range(2, answer1):
        while answer0 % i == 0 and answer1 % i == 0:
            answer0 = answer0 / i
            answer1 = answer1 / i
    
    return [answer0, answer1]