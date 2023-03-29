def solution(angle):
    if angle < 90:
        return 1
    if angle == 90:
        return 2
    if angle < 180:
        return 3
    if angle == 180:
        return 4