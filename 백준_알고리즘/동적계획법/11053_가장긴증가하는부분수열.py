import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N

for i in range(len(seq)):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))