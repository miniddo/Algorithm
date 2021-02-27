import sys
input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
        elif j == 1:
            home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1] 
        else:
            home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]

print(min(home[-1]))