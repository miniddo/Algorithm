import sys
from itertools import combinations

input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

homeArr = list(combinations(home, C))
# print(homeArr)
result = []
for i in homeArr:
  arr = []
  for j in range(len(i)-1):
    arr.append(i[j+1] - i[j])
  arr.sort()
  result.append(arr[0])

print(max(result))

