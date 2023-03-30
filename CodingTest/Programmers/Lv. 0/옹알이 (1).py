def solution(babbling):
    answer = 0
    vowels = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for vowel in vowels:
            babble = babble.replace(vowel, "*")
            
        babble = babble.replace("*", "")
        
        if babble == "":
            answer += 1
    
    return answer