import sys
from collections import deque
input = sys.stdin.readline


def solution(matrix, time):
    x, y = 0, 0 # 뱀 위치
    direc = 1
    dx, dy = 0, 1 # 이동 방향
    count = 1 # 시간
    snack = deque([[x, y]])
    while True:
        x, y = x + dx, y + dy
        if 0 <= x < len(matrix) and 0 <=y < len(matrix) and matrix[x][y] != 1:  # 벽에 부딪치거나, 자기 자신과 만났을 때
            if matrix[x][y] != 2:
                preX, preY = snack.popleft()
                matrix[preX][preY] = 0
            matrix[x][y] = 1
            snack.append([x, y])
            if count in time.keys():
                if time[count] == 'D':  # 오른쪽
                    if direc == 1: dx, dy, direc = 1, 0, 2
                    elif direc == 2: dx, dy, direc = 0, -1, 3
                    elif direc == 3: dx, dy, direc = -1, 0, 4
                    elif direc == 4: dx, dy, direc = 0, 1, 1
                else:   # 왼쪽
                    if direc == 1: dx, dy, direc = -1, 0, 4
                    elif direc == 2: dx, dy, direc = 0, 1, 1
                    elif direc == 3: dx, dy, direc = 1, 0, 2
                    elif direc == 4: dx, dy, direc = 0, -1, 3
            count += 1
        else:
            return count

# 빈 칸 : 0 / 이동 : 1 / 사과 : 2
N = int(input())
matrix = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 2
L = int(input())
time = {}
for _ in range(L):
    x, y = input().split()
    time[int(x)] = y

print(solution(matrix, time))