'''
BFS: 시작 지점에서 가까운 노드부터 차례로 그래프의 모든 노드 탐색

4 6
101111
101010
101011
111011
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

def bfs(i, j):
    
    queue = deque([(i, j)])
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            xx = i + x[k]
            yy = j + y[k]

            if xx >= 0 and xx < N and yy >= 0 and yy < M:
                if maze[xx][yy] == 1:
                    maze[xx][yy] = maze[i][j] + 1
                    queue.append((xx, yy))
                    
    return maze[N-1][M-1] 

print(bfs(0, 0))