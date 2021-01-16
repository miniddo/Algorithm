import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

first = numList[-1]
second = numList[-2]

result = 0
while M > 0:
    for _ in range(K):
        if M == 0: break
        else:
            result += first
            M -= 1
    if M == 0: break
    else:
        result += second
        M -= 1

print(result)

'''
5 8 3
2 4 5 4 6
'''