import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# home: 집 위치 / chicken: 치킨집 위치
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            home.append([i, j])
        if matrix[i][j] == 2:
            chicken.append([i, j])

# 하나의 집을 기준으로 각 치킨집 거리 구하기
distArr = []
for h in home:
    sub = []
    for c in chicken:
        dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
        sub.append(dist)
    distArr.append(sub)

# 폐업할 매장의 수
close = len(chicken) - M

# 폐업할 매장 index 고르기
index = [i for i in range(len(distArr[0]))]
comb = list(combinations(index, close))


result = []
for c in comb:
    # 최솟값
    minDist = []
    for i in range(len(distArr)):
        # 폐업하고 남은 치킨집 거리
        rest = []
        for j in range(len(distArr[i])):
            if j not in c:
                rest.append(distArr[i][j])
        minDist.append(min(rest))
    result.append(sum(minDist))

print(min(result))