import sys
from collections import deque
input = sys.stdin.readline
move = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def dfs(start_x, start_y, end_x, end_y, chase):

  if start_x == end_x and start_y == end_y:
    return 0

  flag = True
  queue = deque([[start_x, start_y, 0]])

  while flag:
    v = queue.popleft()
    for m in move:
      xx = v[0] + m[0]
      yy = v[1] + m[1]

      if xx >= 0 and xx < l and yy >=0 and yy < l:
        if xx == end_x and yy == end_y:
          flag = False
        queue.append([xx, yy, v[2]+1])

  return queue[-1]


T = int(input())
for _ in range(T):
  l = int(input())
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())

  chase = [[0] * l for _ in range(l)]
  result = dfs(start_x, start_y, end_x, end_y, chase)

  print(result[2])
