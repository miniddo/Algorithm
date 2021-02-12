import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus, zero, one = 0, 0, 0

def countPaper(x, y, n):

    global minus, zero, one
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                countPaper(x, y, n//3)
                countPaper(x, y+n//3, n//3)
                countPaper(x, y+n*2//3, n//3)
                countPaper(x+n//3, y, n//3)
                countPaper(x+n//3, y+n//3, n//3)
                countPaper(x+n//3, y+n*2//3, n//3)
                countPaper(x+n*2//3, y, n//3)
                countPaper(x+n*2//3, y+n//3, n//3)
                countPaper(x+n*2//3, y+n*2//3, n//3)
                return 

    if color == -1:  minus += 1
    elif color == 0:    zero += 1
    else:   one += 1



countPaper(0, 0, N)
print(minus)
print(zero)
print(one)