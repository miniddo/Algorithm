import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
direc = list(map(int, input().split()))

dice = [0] * 6
sub = [0] * 6

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

direction = [
    [0, 1, 2, 3, 4, 5],
    [2, 0, 5, 3, 4, 1], # 동쪽
    [1, 5, 0, 3, 4, 2], # 서쪽
    [4, 1, 2, 0, 5, 3], # 북쪽
    [3, 1, 2, 5, 0, 4]  # 남쪽
]

for i in range(k):
    x, y = x + dx[direc[i]], y + dy[direc[i]]
    
    if x < 0 or x >= n or y < 0 or y >= m:
        x, y = x - dx[direc[i]], y - dy[direc[i]]
        continue

    # print(matrix[x][y]) # 지도에 쓰여진 수
    # print(direc[i]) # 이동 방향

    # sub에 dice에 있는 값 복사
    for j in range(6):
        sub[j] = dice[j]
    # 방향 회전
    for j in range(6):
        dice[j] = sub[direction[direc[i]][j]]
        
    if matrix[x][y] == 0:
        matrix[x][y] = dice[5]
    else:
        dice[5] = matrix[x][y]
        matrix[x][y] = 0
    
    print(dice[0])
    


