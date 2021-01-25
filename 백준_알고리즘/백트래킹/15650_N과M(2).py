# from itertools import combinations
# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())

# comb = list(combinations(range(1, N+1), M))
# comb.sort(key=lambda x:x)

# for c in comb:
#     print(' '.join(map(str, c)))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]
visited = [False] * N
result = []

def dfs(x, index):
    if x == M:
        print(' '.join(map(str, result)))
        return
    for i in range(index, N):

        if visited[i]:  
            continue
        
        result.append(numList[i])
        visited[i] = True
        
        dfs(x+1, i+1)
        
        result.pop()
        visited[i] = False

dfs(0, 0)