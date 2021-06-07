import sys

input = sys.stdin.readline
s = list(map(int, input().rstrip()))

dp = []
if s[0] + s[1] > s[0] * s[1]:
    dp.append(s[0] + s[1])
else:
    dp.append(s[0] * s[1])

for i in range(2, len(s)):
    if s[i] + dp[-1] > s[i] * dp[-1]:
        dp.append(s[i] + dp[-1])
    else:
        dp.append(s[i] * dp[-1])

print(dp[-1])