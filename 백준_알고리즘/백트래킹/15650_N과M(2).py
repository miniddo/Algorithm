from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

comb = list(combinations(range(1, N+1), M))
comb.sort(key=lambda x:x)

for c in comb:
    print(' '.join(map(str, c)))