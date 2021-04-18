from itertools import permutations

def solution(numbers):
    
    result = []

    arr = list(numbers)
    for i in range(1, len(arr)+1):
        permu = list(permutations(arr, i))
        permu = list(set(permu))
        for j in permu:
            strNum = int(''.join(j))
            count = 0
            for k in range(2, strNum+1):
                if strNum % k != 0:
                    count += 1
                if strNum % k == 0:
                    break
            if count == strNum - 2:
                result.append(strNum)
    
    result = list(set(result))

    return len(result)



print(solution("17"))
print(solution("011"))