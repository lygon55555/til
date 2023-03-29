def solution(slice, n):
    if n <= slice:
        return 1
    
    if n%slice == 0:
        return n//slice
    
    return n//slice + 1