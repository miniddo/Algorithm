import sys, copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]
grid_weakness = copy.deepcopy(grid)

for i in range(N):
    for j in range(N):
        if grid_weakness[i][j] == 'G':
            grid_weakness[i][j] = 'R'


def checkColor(x, y, value):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if grid[x][y] == value:
        grid[x][y] = 'X'
        checkColor(x-1, y, value)
        checkColor(x+1, y, value)
        checkColor(x, y-1, value)
        checkColor(x, y+1, value)
        return value
    return False

def checkColor_weakness(x, y, value):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if grid_weakness[x][y] == value:
        grid_weakness[x][y] = 'X'
        checkColor_weakness(x-1, y, value)
        checkColor_weakness(x+1, y, value)
        checkColor_weakness(x, y-1, value)
        checkColor_weakness(x, y+1, value)
        return value
    return False


result, result_w = 0, 0
for i in range(N):
    for j in range(N):
        if checkColor(i, j, 'R') == 'R': result += 1
        if checkColor(i, j, 'G') == 'G': result += 1
        if checkColor(i, j, 'B') == 'B': result += 1

        if checkColor_weakness(i, j, 'R') == 'R': result_w += 1
        if checkColor_weakness(i, j, 'B') == 'B': result_w += 1

print(result, result_w)