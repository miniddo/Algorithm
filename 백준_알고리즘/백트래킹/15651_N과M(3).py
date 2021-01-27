import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]
result = []

def dfs(x):
    if x == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        result.append(numList[i])
        dfs(x+1)     
        result.pop()

dfs(0)