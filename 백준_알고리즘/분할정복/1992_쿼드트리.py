import sys
input = sys.stdin.readline

N = int(input())
tree = [list(input().rstrip()) for _ in range(N)]
result = []

def countTree(x, y, n):

    global result
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if tree[i][j] != color:
                countTree(x, y, n//2)
                countTree(x, y+n//2, n//2)
                countTree(x+n//2, y, n//2)
                countTree(x+n//2, y+n//2, n//2)
                return
    
    if color == '1':
        result.append('1')
    else:
        result.append('0')


countTree(0, 0, N)
print(result)

