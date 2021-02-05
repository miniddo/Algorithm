import sys
from itertools import combinations

input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

homeArr = list(combinations(home, C))
result = 0

print(homeArr)
for i in homeArr:
  print(i[0], i[-1])


