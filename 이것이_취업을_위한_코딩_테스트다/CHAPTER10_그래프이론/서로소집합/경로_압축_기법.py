'''
경로 압축 기법

각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 루트 노드가 바로 부모 노드가 된다.
'''

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent_table, a, b):
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)
    if a < b:
        parent_table[b] = a
    else:
        parent_table[a] = b

n, v = map(int, input().split())
parent_table = [0] * (n+1)

# 처음은 자기 자신으로 부모 초기화
for i in range(1, n+1):
    parent_table[i] = i

for _ in range(v):
    a, b = map(int, input().split())
    union_parent(parent_table, a, b)

print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, n+1):
    print(find_parent(parent_table, i), end=' ')

print()

print('부모 테이블 : ', end=' ')
for i in range(1, n+1):
    print(parent_table[i], end=' ')

'''
6 4
1 4
2 3
2 4
5 6

각 원소가 속한 집합 : 1 1 1 1 5 5
부모 테이블 : 1 1 2 1 5 5
'''