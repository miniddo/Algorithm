from collections import deque
import math

def solution(s):

    if len(s) == 1:
        return 1

    answer = ''
    for i in range(1, len(s)//2+1):

        q = deque([])
        for j in range(math.ceil(len(s)/i)):
            if(len(s[j*i:j*i+i])) == i:
                q.append(s[j*i:j*i+i])
            else:
                q.append(s[j*i:])
        
        sub = []
        result = ''
        while True:
            if not sub:
                sub.append(q.popleft())
                continue
            if not q:
                if(len(sub) == 1):
                    result += sub[0]
                else: 
                    result += str(len(sub)) + sub[0]
                sub.clear()
                break

            if sub[-1] == q[0]:
                sub.append(q.popleft())
            else:
                if len(sub) == 1:
                    result += sub[0]
                else: 
                    result += str(len(sub)) + sub[0]
                sub.clear()
        
        if answer == '':
            answer = result
        elif len(result) < len(answer):
            answer = result 
    
    return len(answer)


# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('xababcdcdababcdcd'))
print(solution('a'))