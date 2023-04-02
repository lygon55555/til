def solution(name, yearning, photo):
    dic = {}
    answer = []
    
    for i in range(0, len(name)):
        dic[name[i]] = yearning[i]
    
    for p in photo:
        score = 0
        for name in p:
            if name in dic:
                score += dic[name]
        answer.append(score)
    
    return answer