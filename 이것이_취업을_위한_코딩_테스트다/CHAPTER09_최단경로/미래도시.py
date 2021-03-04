import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        graph[i][j] = 0
      else:
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


dist = graph[1][k] + graph[k][x]

if dist == INF:
  print("-1")
else:
  print(dist)


'''
최단 거리 알고리즘
N(노드의 개수)의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 사용한다.
'''

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''