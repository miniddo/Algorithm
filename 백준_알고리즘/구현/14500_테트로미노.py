import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 회전(90도)
def rotate(n, m, matrix):
    result = []
    for i in range(m):
        ret = []
        for j in range(n):
            ret.append(matrix[j][i])
        result.append(ret)
    return result

# 대칭
def symmetry(n, m, matrix):
    result = []
    for i in range(n):
        ret = []
        for j in range(m-1, -1, -1):
            ret.append(matrix[i][j])
        result.append(ret)
    return result


# 기본
count = 0
for i in range(n):
    for j in range(m):
        if j+3 >= m: break
        if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3] > count:
            count =  matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]

# 90도 회전
matrix_90 = rotate(n, m, matrix)
for i in range(len(matrix_90)):
    for j in range(i):
        if j+3 >= i: break
        if matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i][j+3] > count:
            count =  matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i][j+3]


# 180도 회전

# 270도 회전


matrix_symmetry = symmetry(n, m, matrix)

# 기본 + 대칭
for i in range(n):
    for j in range(m):
        if j+3 >= m: break
        if matrix_symmetry[i][j] + matrix_symmetry[i][j+1] + matrix_symmetry[i][j+2] + matrix_symmetry[i][j+3] > count:
            count =  matrix_symmetry[i][j] + matrix_symmetry[i][j+1] + matrix_symmetry[i][j+2] + matrix_symmetry[i][j+3]

# 90도 회전 + 대칭
matrix_90_sym = rotate(n, m, matrix_symmetry)
for i in range(len(matrix_90)):
    for j in range(i):
        if j+3 >= i: break
        if matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i][j+3] > count:
            count =  matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i][j+3]

# 180도 회전 + 대칭

# 270도 회전 + 대칭

print(count)