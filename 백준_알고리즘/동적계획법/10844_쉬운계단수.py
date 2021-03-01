import sys
input = sys.stdin.readline

N = int(input())
dp  = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
num = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if N == 1:
    print(sum(dp))
else:
    for _ in range(1, N):
        dp = num
        for i in range(len(dp)):
            if i == 0:
                num[i] = dp[i+1]
            elif i == 9:
                num[i] = dp[i-1]
            else:
                num[i] = dp[i-1] + dp[i+1]

print('result', dp, num)