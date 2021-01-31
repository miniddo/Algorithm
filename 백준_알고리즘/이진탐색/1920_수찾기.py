import sys
input = sys.stdin.readline

def isNumber(b):
    start, end = 0, len(A)-1
    flag = False
    while start <= end:
        mid = (start + end)//2
        if A[mid] == b:
            flag = True
            return 1
        elif A[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    if flag == False:
        return 0


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

for b in B:
    print(isNumber(b))