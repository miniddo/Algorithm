import sys
input = sys.stdin.readline

n, v = map(int, input().split())
parent_table = [0] * (n+1)

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

for i in range(1, n+1):
    parent_table[i] = i

cycle = False

for i in range(v):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종류 (루트 노트가 같을 때)
    if find_parent(parent_table, a) == find_parent(parent_table, b):
        cycle = True
        break
    # 사이클이 발생하지 않은 경우, union 연산 수행
    else:
        union_parent(parent_table, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')

'''
3 3 
1 2
1 3
2 3
'''