import sys
import math
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())    # n: 우주신의 개수, m: 이미 연결된 통로 개수
universe = [list(map(int, input().split())) for _ in range(n)]
universe.insert(0, [0, 0])
dists = []
parent = [0] * (n+1)
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b = map(int, input().split())
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = math.sqrt(math.pow(universe[j][0] - universe[i][0], 2) + math.pow(universe[j][1] - universe[i][1], 2))
        cost = round(cost, 2)
        dists.append((cost, i, j))

dists.sort()

for dist in dists:
    cost, a, b = dist
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


print("%0.2f" % result)

'''
4 1
1 1
3 1
2 3
4 3
1 4
'''