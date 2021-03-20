import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def solution(r, c, d, clean):

    if matrix[r][c] == 0:
        clean += 1
        matrix[r][c] = 2
    
    if d == 0:  # 북쪽(위쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] == 1:
            return clean
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return solution(r+1, c, d, clean)
        if matrix[r][c-1] == 1 or matrix[r][c-1] == 2:
            return solution(r, c, 3, clean)
        if matrix[r][c-1] == 0:
            return solution(r, c-1, 3, clean)
    elif d == 1: # 동쪽(오른쪽)
        if matrix[r][c-1] == 1 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return clean
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return solution(r, c-1, d, clean)
        if matrix[r-1][c] == 1 or matrix[r-1][c] == 2:
            return solution(r, c, 0, clean)
        if matrix[r-1][c] == 0:
            return solution(r-1, c, 0, clean)
    elif d == 2: # 남쪽(아래쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] == 1 and matrix[r+1][c] != 0:
            return clean
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return solution(r-1, c, d, clean) 
        if matrix[r][c+1] == 1 or matrix[r][c+1] == 2:
            return solution(r, c, 1, clean)
        if matrix[r][c+1] == 0:
            return solution(r, c+1, 1, clean)
    elif d == 3: # 서쪽(왼쪽)
        if matrix[r][c-1] != 0 and matrix[r][c+1] == 1 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return clean
        if matrix[r][c-1] != 0 and matrix[r][c+1] != 0 and matrix[r-1][c] != 0 and matrix[r+1][c] != 0:
            return solution(r, c+1, d, clean) 
        if matrix[r+1][c] == 1 or matrix[r+1][c] == 2:
            return solution(r, c, 2, clean)
        if matrix[r+1][c] == 0:
            return solution(r+1, c, 2, clean)

print(solution(r, c, d, 0))