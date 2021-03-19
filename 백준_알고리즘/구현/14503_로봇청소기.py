import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

clean = 0
flag = True

while flag:
    if matrix[r][c] == 0:
        clean += 1
        matrix[r][c] = 2
    
    if d == 0:  # 북쪽(위쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] == 1:
            flag = False
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            r, c = r+1, c 
        if matrix[r][c-1] == 1:
            d = 3
        if matrix[r][c-1] == 0:
            d = 3
            r, c = r, c-1
    elif d == 1: # 동쪽(오른쪽)
        if matrix[r][c-1] == 1 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            flag = False
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            r, c = r, c-1 
        if matrix[r-1][c] == 1:
            d = 0
        if matrix[r-1][c] == 0:
            d = 0
            r, c = r-1, c
    elif d == 2: # 남쪽(아래쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] == 1 and matrix[r+1][c] != 0:
            flag = False
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            r, c = r-1, c 
        if matrix[r][c+1] == 1:
            d = 1
        if matrix[r][c+1] == 0:
            d = 1
            r, c = r, c+1
    elif d == 3: # 서쪽(왼쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] == 1 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            flag = False
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            r, c = r, c+1 
        if matrix[r+1][c] == 1:
            d = 2
        if matrix[r+1][c] == 0:
            d = 2
            r, c = r+1, c


print(clean)