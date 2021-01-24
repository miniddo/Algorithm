from itertools import permutations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

number = [i for i in range(1, N+1)]
permu = list(permutations(number, M))

for p in permu:
    print(' '.join(map(str, p)))