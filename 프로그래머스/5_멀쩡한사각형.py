import math

def solution(w,h):

    broke = w + h - math.gcd(w, h)
    answer = w * h - broke

    return answer
        
    


print(solution(8, 12))