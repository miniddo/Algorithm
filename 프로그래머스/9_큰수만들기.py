from itertools import combinations

def solution(number, k):

    arr = [[i, number[i]] for i in range(len(number))]
    idx = [i for i in range(len(arr))]
    comb = list(combinations(idx, k))

    result = '0'
    for c in comb:
        sub = ''
        for a in arr:
            if a[0] not in c:
                sub += a[1]
        if int(result) < int(sub):
            result = sub
    
    return result


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))


'''
def solution(number, k):
    
    number = list(number)
    stack = [number[0]]
    count = 0
    
    for i in range(1, len(number)):
        if count == k:
            break
        if number[i] <= stack[-1]:
            stack.append(number[i])
        else:
            while True:
                if count == k:
                    break
                if len(stack) != 0:
                    if number[i] <= stack[-1]:
                        stack.append(number[i])
                        break
                    else:
                        stack.pop()
                        count += 1
                else:
                    stack.append(number[i])
                    break
    
    if count != k:
        number = number[:-k]
        stack = list(map(str, number))
        result = ''.join(stack)
        return result
                    
    need = len(number) - k - len(stack)
    new_stack = []
    if need != 0:
        new_stack = list(number[-need:])
    
    stack.extend(new_stack)
    
    return ''.join(stack)
'''