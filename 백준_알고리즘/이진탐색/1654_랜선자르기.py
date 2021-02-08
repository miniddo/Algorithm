# K개의 랜선
# 모두 N개의 같은 길이의 랜선

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for i in range(K)]
lan.sort()

start, end = 1, lan[-1]

while start <= end:
    mid = (start + end)//2
    target = 0
    for i in lan:
        target += (i // mid)

    if target < N:
        end = mid - 1
    else:   # 잘라낸 개수가 기준보다 많다면, 더 큰 단위로 자른다.(최댓값)
        result = mid
        start = mid + 1

print(result)
# print(end)