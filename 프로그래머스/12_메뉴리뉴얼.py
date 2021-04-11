from itertools import combinations
from collections import Counter

def solution(orders, course):

    # 각 주문건을 오름차순 정렬한다.
    _orders = []
    for o in orders:
        _orders.append(sorted(list(o)))

    # course에서 orders의 길이 초과는 포함하지 않는다.
    _orders.sort(key=lambda x:len(x))
    _max = len(_orders[-1])
    
    _course = []
    for c in course:
        if c <= _max:
            _course.append(c)
    
    # 조건에 맞게 조합한다.
    result = []
    for i in _course:
        # 각 course 개수에 맞게 조합한다.
        sub1 = []
        for j in _orders:
            sub1.append(list(combinations(j, i)))
        # 하나의 배열로 합친다.
        sub2 = []
        for x in sub1:
            for y in x:
                sub2.append(y)
        # 같은 개수의 조합이라면 최대로 많이 주문한 것만 넣는다.
        sub3 = list(Counter(sub2).items())
        sub3.sort(key=lambda x:-x[1])
        subMax = sub3[0][1]
        for s in sub3:
            if s[1] > 1 and s[1] >= subMax:
                result.append(s[0])
    
    # 문자열로 join 한다.
    answer = []
    for r in result:
        answer.append(''.join(list(r)))

    answer.sort()  
    return answer




print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))