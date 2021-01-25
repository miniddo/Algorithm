import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]
visited = [False] * N
result = []

def dfs(x):
    if x == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if visited[i]:  
            continue
        
        result.append(numList[i])
        visited[i] = True
        
        dfs(x+1)
        
        result.pop()
        visited[i] = False

dfs(0)