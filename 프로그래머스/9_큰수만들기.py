from itertools import combinations

def solution(number, k):

    arr = [[i, number[i]] for i in range(len(number))]
    idx = [i for i in range(len(arr))]
    comb = list(combinations(idx, k))

    result = '0'
    for c in comb:
        # print(c)
        sub = ''
        # print(arr)
        for a in arr:
            # print('--', a)
            if a[0] not in c:
                # print('**', a)
                sub += a[1]
        if int(result) < int(sub):
            result = sub
    
    return result


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))