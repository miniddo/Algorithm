'''
신장트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 = 트리의 성립 조건
크루스칼 알고리즘 : 가능한 한 최소한의 비용으로 신장 트리를 찾아야 할 때 (그리디 알고리즘)
'''

import sys
input = sys.stdin.readline

def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

def union_parent(parent_table, a, b):
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)
    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b


n, v = map(int, input().split())
parent_table = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent_table[i] = i

for i in range(v):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 오름차순 정렬 (비용 순)
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않을 때
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)    # 합집합 수행
        result += cost                      # 비용 추가

print(result)

'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''