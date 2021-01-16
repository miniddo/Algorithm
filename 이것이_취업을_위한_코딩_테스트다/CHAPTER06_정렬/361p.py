from collections import Counter

def solution(N, stages):
    
    notClear = Counter(stages)
    result = []
    
    for i in range(1, N+1):
        # 1의 개수 / 1보다 크거나 같은 개수
        top = notClear.get(i, 0)
        bottom = len(list(filter(lambda x:x>=i, stages)))
        
        if bottom == 0:
            result.append((i, 0))
        else:
            result.append((i, top/bottom))
    
    result.sort(key=lambda x:(-x[1],x[0]))
    
    answer = []
    for i in result:
        answer.append(i[0])
    
    return answer