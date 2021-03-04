import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

city, time = 0, 0

for i in range(1, n+1):
    if distance[i] != INF:
        city += 1
        time = max(time, distance[i])

print(city-1, time)


'''
3 2 1
1 2 4
1 3 2
'''