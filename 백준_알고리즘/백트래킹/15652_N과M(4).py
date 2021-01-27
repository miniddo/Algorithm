import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = [i+1 for i in range(N)] 
arr = []

def DFS(x, idx):
    if x == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, N):
        arr.append(numList[i])
        DFS(x+1, i)
        arr.pop()

DFS(0, 0)


