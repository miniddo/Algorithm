import sys
from collections import deque
input = sys.stdin.readline

def dfs(queue):
    while queue:
        node = queue.popleft()
        i, j, c = node[0], node[1], node[2]
        for k in range(4):
            xx = i + x[k]
            yy = j + y[k]

            if xx >= 0 and xx < N and yy >=0 and yy < M:
                if tomato[xx][yy] == 0:
                    tomato[xx][yy] = 1
                    queue.append([xx, yy, c+1])
    
    return c

def isTomato(result, tomato):
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
    return result

M, N = map(int, input().split())

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
cnt = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j, cnt])

result = dfs(queue)
print(isTomato(result, tomato))