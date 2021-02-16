'''
음료수 얼려먹기

N = 4,  M = 5

4 5
00110
00011
11111
00000
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
beverage = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return False
    if beverage[i][j] == 0:
        beverage[i][j] = 1
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)