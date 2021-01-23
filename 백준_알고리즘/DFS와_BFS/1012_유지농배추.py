import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    graph = [[0] * M for _ in range(N)]

    for a in arr:
        graph[a[1]][a[0]] = 1

    def dfs(i, j):
        if i < 0 or i >=N or j < 0 or j >= M:
            return False
        if graph[i][j] == 1:
            graph[i][j] = 0
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j) 
            dfs(i, j+1)
            return True
        return False

    result = 0
    for x in range(N):
        for y in range(M):
            if dfs(x, y) == True:
                result += 1

    print(result)