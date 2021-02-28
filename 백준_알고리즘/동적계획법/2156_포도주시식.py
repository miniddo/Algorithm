import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input().rstrip()) for _ in range(n)]

dp = [0] * (n)

for i in range(n):
    if i == 0:
        dp[0] = wine[0]
    elif i == 1:
        dp[1] = wine[0] + wine[1]
    else:
        dp[i] = max(dp[i-1], wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2])

print(dp[-1])