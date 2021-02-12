import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def solution(A, B):
    if B == 1:
        return A % C
    else:
        value = solution(A, B//2)
        if B % 2 == 0:
            return value * value % C
        else:
            return value * value * A % C


print(solution(A, B))

# print(pow(A, B, C))