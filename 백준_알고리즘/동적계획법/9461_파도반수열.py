import sys
input = sys.stdin.readline

def solution(N):

    dp = [0] * 101
    dp[0], dp[1], dp[2] = 1, 1, 1

    for i in range(3, N+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[N-1]

T = int(input())
for _ in range(T):
    print(solution(int(input())))