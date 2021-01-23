import sys
from collections import deque
input = sys.stdin.readline

def bfs(queue):
    while queue:
        node = queue.popleft()
        h, i, j, c = node[0], node[1], node[2], node[3]

        # 왼쪽, 오른쪽, 앞, 뒤
        for k in range(4):
            xx = i + x[k]
            yy = j + y[k]

            if xx >= 0 and xx < N and yy >= 0 and yy < M:
                if allTomato[h][xx][yy] == 0:
                    allTomato[h][xx][yy] = 1
                    queue.append([h, xx, yy, c+1])

        # 위
        top = h - 1
        if top >=0:
            if allTomato[top][i][j] == 0:
                allTomato[top][i][j] = 1
                queue.append([top, i, j, c+1])
        
        # 아래
        bottom = h + 1
        if bottom < H:
            if allTomato[bottom][i][j] == 0:
                allTomato[bottom][i][j] = 1
                queue.append([bottom, i, j, c+1])        

    return c

def isTomato(result):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if allTomato[h][i][j] == 0:
                    return -1
    return result

M, N, H = map(int, input().split())

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

allTomato = []
for _ in range(H):
    tomato = [list(map(int, input().split())) for _ in range(N)]
    allTomato.append(tomato)

queue = deque([])
cnt = 0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if allTomato[h][i][j] == 1:
                queue.append([h, i, j, cnt])

result = bfs(queue)
print(isTomato(result))