import sys
from collections import deque
input = sys.stdin.readline
move = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def bfs():

  queue = deque([[start_x, start_y]])
  chase[start_x][start_y] = 1

  while queue:
    v = queue.popleft()

    if end_x == v[0] and end_y == v[1]:
      return chase[v[0]][v[1]] - 1
      
    for m in move:
      xx = v[0] + m[0]
      yy = v[1] + m[1]

      if xx < 0 or xx >= l or yy < 0 or yy >= l:
        continue
      else:
        if chase[xx][yy] == 0:
          chase[xx][yy] = chase[v[0]][v[1]] + 1
          queue.append([xx, yy])


T = int(input())
for _ in range(T):
  l = int(input())
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())

  chase = [[0] * l for _ in range(l)]
  result = bfs()

  print(result)
