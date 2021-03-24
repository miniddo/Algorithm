import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 90도 회전
def rotate_90(n, m, matrix):
    result = []
    for i in range(m):
        ret = []
        for j in range(n-1, -1, -1):
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


def type1(n, m, matrix):

    count = 0
    
    # 기본
    for i in range(n):
        for j in range(m):
            if j+3 >= m: break
            if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3] > count:
                count =  matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]

    # 90도 회전
    matrix_90 = rotate_90(n, m, matrix)
    for i in range(len(matrix_90)):
        for j in range(len(matrix_90[0])):
            if j+3 >= len(matrix_90[0]): break
            if matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i][j+3] > count:
                count =  matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i][j+3]

    matrix = symmetry(n, m, matrix)
    # 기본 + 대칭
    for i in range(n):
        for j in range(m):
            if j+3 >= m: break
            if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3] > count:
                count =  matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]

    # 90도 회전 + 대칭
    matrix_90_sym = rotate_90(n, m, matrix)
    for i in range(len(matrix_90_sym)):
        for j in range(len(matrix_90_sym[0])):
            if j+3 >= len(matrix_90_sym[0]): break
            if matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i][j+3] > count:
                count =  matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i][j+3]

    return count

def type2(n, m, matrix):

    count = 0
    
    # 기본
    for i in range(n):
        for j in range(m):
            if j+1 >= m or i+1 >=n: break
            if matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1] > count:
                count =  matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]

    return count

def type3(n, m, matrix):

    count = 0
    
    # 기본
    for i in range(n):
        for j in range(m):
            if i+2 >=n or j+1 >= m: break
            if matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1] > count:
                count =  matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]

    # 90도 회전
    matrix_90 = rotate_90(n, m, matrix)
    for i in range(len(matrix_90)):
        for j in range(len(matrix_90[0])):
            if i+2 >=len(matrix_90) or j+1 >= len(matrix_90[0]): break
            if matrix_90[i][j] + matrix_90[i+1][j] + matrix_90[i+2][j] + matrix_90[i+2][j+1] > count:
                count =  matrix_90[i][j] + matrix_90[i+1][j] + matrix_90[i+2][j] + matrix_90[i+2][j+1]
    
    # 180도 회전
    matrix_180 = rotate_90(len(matrix_90), len(matrix_90[0]), matrix_90)
    for i in range(len(matrix_180)):
        for j in range(len(matrix_180[0])):
            if i+2 >=len(matrix_180) or j+1 >= len(matrix_180[0]): break
            if matrix_180[i][j] + matrix_180[i+1][j] + matrix_180[i+2][j] + matrix_180[i+2][j+1] > count:
                count =  matrix_180[i][j] + matrix_180[i+1][j] + matrix_180[i+2][j] + matrix_180[i+2][j+1]

    # 270도 회전
    matrix_270 = rotate_90(len(matrix_180), len(matrix_180[0]), matrix_180)
    for i in range(len(matrix_270)):
        for j in range(len(matrix_270[0])):
            if i+2 >=len(matrix_270) or j+1 >= len(matrix_270[0]): break
            if matrix_270[i][j] + matrix_270[i+1][j] + matrix_270[i+2][j] + matrix_270[i+2][j+1] > count:
                count =  matrix_270[i][j] + matrix_270[i+1][j] + matrix_270[i+2][j] + matrix_270[i+2][j+1]


    matrix = symmetry(n, m, matrix)
    # 기본 + 대칭
    for i in range(n):
        for j in range(m):
            if i+2 >=n or j+1 >= m: break
            if matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1] > count:
                count =  matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]

    # 90도 회전 + 대칭
    matrix_90_sym = rotate_90(n, m, matrix)
    for i in range(len(matrix_90)):
        for j in range(len(matrix_90[0])):
            if i+2 >=len(matrix_90) or j+1 >= len(matrix_90[0]): break
            if matrix_90_sym[i][j] + matrix_90_sym[i+1][j] + matrix_90_sym[i+2][j] + matrix_90_sym[i+2][j+1] > count:
                count =  matrix_90_sym[i][j] + matrix_90_sym[i+1][j] + matrix_90_sym[i+2][j] + matrix_90_sym[i+2][j+1]

    # 180도 회전 + 대칭
    matrix_180_sym = rotate_90(len(matrix_90_sym), len(matrix_90_sym[0]), matrix_90_sym)
    for i in range(len(matrix_180)):
        for j in range(len(matrix_180[0])):
            if i+2 >=len(matrix_180) or j+1 >= len(matrix_180[0]): break
            if matrix_180_sym[i][j] + matrix_180_sym[i+1][j] + matrix_180_sym[i+2][j] + matrix_180_sym[i+2][j+1] > count:
                count =  matrix_180_sym[i][j] + matrix_180_sym[i+1][j] + matrix_180_sym[i+2][j] + matrix_180_sym[i+2][j+1]

    # 270도 회전 + 대칭
    matrix_270_sym = rotate_90(len(matrix_180_sym), len(matrix_180_sym[0]), matrix_180_sym)
    for i in range(len(matrix_270)):
        for j in range(len(matrix_270[0])):
            if i+2 >=len(matrix_270) or j+1 >= len(matrix_270[0]): break
            if matrix_270_sym[i][j] + matrix_270_sym[i+1][j] + matrix_270_sym[i+2][j] + matrix_270_sym[i+2][j+1] > count:
                count =  matrix_270_sym[i][j] + matrix_270_sym[i+1][j] + matrix_270_sym[i+2][j] + matrix_270_sym[i+2][j+1]

    return count

def type4(n, m, matrix):

    count = 0
    
    # 기본
    for i in range(n):
        for j in range(m):
            if i+2 >=n or j+1 >= m: break
            if matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1] > count:
                count =  matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]

    # 90도 회전
    matrix_90 = rotate_90(n, m, matrix)
    for i in range(len(matrix_90)):
        for j in range(len(matrix_90[0])):
            if i+2 >=len(matrix_90) or j+1 >= len(matrix_90[0]): break
            if matrix_90[i][j] + matrix_90[i+1][j] + matrix_90[i+1][j+1] + matrix_90[i+2][j+1] > count:
                count =  matrix_90[i][j] + matrix_90[i+1][j] + matrix_90[i+1][j+1] + matrix_90[i+2][j+1]
    
    # 180도 회전
    matrix_180 = rotate_90(len(matrix_90), len(matrix_90[0]), matrix_90)
    for i in range(len(matrix_180)):
        for j in range(len(matrix_180[0])):
            if i+2 >=len(matrix_180) or j+1 >= len(matrix_180[0]): break
            if matrix_180[i][j] + matrix_180[i+1][j] + matrix_180[i+1][j+1] + matrix_180[i+2][j+1] > count:
                count = matrix_180[i][j] + matrix_180[i+1][j] + matrix_180[i+1][j+1] + matrix_180[i+2][j+1]

    # 270도 회전
    matrix_270 = rotate_90(len(matrix_180), len(matrix_180[0]), matrix_180)
    for i in range(len(matrix_270)):
        for j in range(len(matrix_270[0])):
            if i+2 >=len(matrix_270) or j+1 >= len(matrix_270[0]): break
            if matrix_270[i][j] + matrix_270[i+1][j] + matrix_270[i+1][j+1] + matrix_270[i+2][j+1] > count:
                count = matrix_270[i][j] + matrix_270[i+1][j] + matrix_270[i+1][j+1] + matrix_270[i+2][j+1]


    matrix = symmetry(n, m, matrix)
    # 기본 + 대칭
    for i in range(n):
        for j in range(m):
            if i+2 >=n or j+1 >= m: break
            if matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1] > count:
                count = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]

    # 90도 회전 + 대칭
    matrix_90_sym = rotate_90(n, m, matrix)
    for i in range(len(matrix_90_sym)):
        for j in range(len(matrix_90_sym[0])):
            if i+2 >=len(matrix_90_sym) or j+1 >= len(matrix_90_sym[0]): break
            if matrix_90_sym[i][j] + matrix_90_sym[i+1][j] + matrix_90_sym[i+1][j+1] + matrix_90_sym[i+2][j+1] > count:
                count =  matrix_90_sym[i][j] + matrix_90_sym[i+1][j] + matrix_90_sym[i+1][j+1] + matrix_90_sym[i+2][j+1]

    # 180도 회전 + 대칭
    matrix_180_sym = rotate_90(len(matrix_90_sym), len(matrix_90_sym[0]), matrix_90_sym)
    for i in range(len(matrix_180_sym)):
        for j in range(len(matrix_180_sym[0])):
            if i+2 >=len(matrix_180_sym) or j+1 >= len(matrix_180_sym[0]): break
            if matrix_180_sym[i][j] + matrix_180_sym[i+1][j] + matrix_180_sym[i+1][j+1] + matrix_180_sym[i+2][j+1] > count:
                count =  matrix_180_sym[i][j] + matrix_180_sym[i+1][j] + matrix_180_sym[i+1][j+1] + matrix_180_sym[i+2][j+1]

    # 270도 회전 + 대칭
    matrix_270_sym = rotate_90(len(matrix_180_sym), len(matrix_180_sym[0]), matrix_180_sym)
    for i in range(len(matrix_270_sym)):
        for j in range(len(matrix_270_sym[0])):
            if i+2 >=len(matrix_270_sym) or j+1 >= len(matrix_270_sym[0]): break
            if matrix_270_sym[i][j] + matrix_270_sym[i+1][j] + matrix_270_sym[i+1][j+1] + matrix_270_sym[i+2][j+1] > count:
                count =  matrix_270_sym[i][j] + matrix_270_sym[i+1][j] + matrix_270_sym[i+1][j+1] + matrix_270_sym[i+2][j+1]

    return count

def type5(n, m, matrix):

    count = 0
    
    # 기본
    for i in range(n):
        for j in range(m):
            if i+1 >=n or j+2 >= m: break
            if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] > count:
                count =  matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]

    # 90도 회전
    matrix_90 = rotate_90(n, m, matrix)
    for i in range(len(matrix_90)):
        for j in range(len(matrix_90[0])):
            if i+1 >=len(matrix_90) or j+2 >= len(matrix_90[0]): break
            if matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i+1][j+1] > count:
                count = matrix_90[i][j] + matrix_90[i][j+1] + matrix_90[i][j+2] + matrix_90[i+1][j+1]
    
    # 180도 회전
    matrix_180 = rotate_90(len(matrix_90), len(matrix_90[0]), matrix_90)
    for i in range(len(matrix_180)):
        for j in range(len(matrix_180[0])):
            if i+1 >=len(matrix_180) or j+2 >= len(matrix_180[0]): break
            if matrix_180[i][j] + matrix_180[i][j+1] + matrix_180[i][j+2] + matrix_180[i+1][j+1] > count:
                count = matrix_180[i][j] + matrix_180[i][j+1] + matrix_180[i][j+2] + matrix_180[i+1][j+1]

    # 270도 회전
    matrix_270 = rotate_90(len(matrix_180), len(matrix_180[0]), matrix_180)
    for i in range(len(matrix_270)):
        for j in range(len(matrix_270[0])):
            if i+1 >=len(matrix_270) or j+2 >= len(matrix_270[0]): break
            if matrix_270[i][j] + matrix_270[i][j+1] + matrix_270[i][j+2] + matrix_270[i+1][j+1] > count:
                count = matrix_270[i][j] + matrix_270[i][j+1] + matrix_270[i][j+2] + matrix_270[i+1][j+1]


    matrix = symmetry(n, m, matrix)
    # 기본 + 대칭
    for i in range(n):
        for j in range(m):
            if i+1 >=n or j+2 >= m: break
            if matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] > count:
                count = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]

    # 90도 회전 + 대칭
    matrix_90_sym = rotate_90(n, m, matrix)
    for i in range(len(matrix_90_sym)):
        for j in range(len(matrix_90_sym[0])):
            if i+1 >=len(matrix_90_sym) or j+2 >= len(matrix_90_sym[0]): break
            if matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i+1][j+1] > count:
                count = matrix_90_sym[i][j] + matrix_90_sym[i][j+1] + matrix_90_sym[i][j+2] + matrix_90_sym[i+1][j+1]

    # 180도 회전 + 대칭
    matrix_180_sym = rotate_90(len(matrix_90_sym), len(matrix_90_sym[0]), matrix_90_sym)
    for i in range(len(matrix_180_sym)):
        for j in range(len(matrix_180_sym[0])):
            if i+1 >=len(matrix_180_sym) or j+2 >= len(matrix_180_sym[0]): break
            if matrix_180_sym[i][j] + matrix_180_sym[i][j+1] + matrix_180_sym[i][j+2] + matrix_180_sym[i+1][j+1] > count:
                count = matrix_180_sym[i][j] + matrix_180_sym[i][j+1] + matrix_180_sym[i][j+2] + matrix_180_sym[i+1][j+1]

    # 270도 회전 + 대칭
    matrix_270_sym = rotate_90(len(matrix_180_sym), len(matrix_180_sym[0]), matrix_180_sym)
    for i in range(len(matrix_270_sym)):
        for j in range(len(matrix_270_sym[0])):
            if i+1 >=len(matrix_270_sym) or j+2 >= len(matrix_270_sym[0]): break
            if matrix_270_sym[i][j] + matrix_270_sym[i][j+1] + matrix_270_sym[i][j+2] + matrix_270_sym[i+1][j+1] > count:
                count = matrix_270_sym[i][j] + matrix_270_sym[i][j+1] + matrix_270_sym[i][j+2] + matrix_270_sym[i+1][j+1]

    return count

result = []

count1 = type1(n, m, matrix)
count2 = type2(n, m, matrix)
count3 = type3(n, m, matrix)
count4 = type4(n, m, matrix)
count5 = type5(n, m, matrix)

result.append(count1)
result.append(count2)
result.append(count3)
result.append(count4)
result.append(count5)

print(max(result))