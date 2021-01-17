import sys
input = sys.stdin.readline

N = int(input())

def dfs(house, cnt, i, j):

    house[i][j] = 0
    x, y = [1, -1, 0, 0], [0, 0, 1, -1]
    for k in range(4):
        xx = i + x[k]
        yy = j + y[k]
        if xx >= 0 and xx < N and yy >=0 and yy < N:
            if house[xx][yy] == 1:
                cnt = dfs(house, cnt+1, xx, yy)
    return cnt


house = [list(map(int, input().rstrip())) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            result.append(dfs(house, 1, i, j))

print(len(result))
for a in sorted(result):
    print(a)