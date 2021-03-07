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

n = int(input())
parent = [0] * (n+1)

star = [[0, 0] for _ in range(n+1)]
dists = []
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    a, b = map(float, input().split())
    star[i][0], star[i][1] = a, b

for i in range(1, n+1):
    for j in range(i+1, n+1):
        # print(i, star[i], j, star[j])
        cost = math.sqrt(math.pow(star[j][0] - star[i][0], 2) + math.pow(star[j][1] - star[i][1], 2))
        cost = round(cost, 2)
        dists.append((cost, i, j))

# print(dists)
dists.sort()

for dist in dists:
    cost, a, b = dist
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

    