'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 0

def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    if house[i][j] == 1:
        house[i][j] = 0
        global cnt
        cnt += 1

        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False


result = 0
arr = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            arr.append(cnt)
            cnt = 0

arr.sort()

print(result)
for a in range(arr):
    print(a)

# https://joosjuliet.github.io/2667/