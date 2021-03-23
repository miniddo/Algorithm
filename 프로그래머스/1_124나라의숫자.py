def solution(n):

    if n <= 3:
        return '124'[n-1]
    else:
        return solution((n-1)//3) + '124'[(n-1)%3]


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(10))
