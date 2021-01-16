import sys
input = sys.stdin.readline

N = int(input())
home = list(map(int, input().split()))

home.sort()

# 1. 시간초과
# left, right = home[0], home[-1]

# total = 100000
# result = 0
# for i in range(left, right+1):
#     sub = 0
#     for j in home:
#         sub += abs(i-j)
#     if sub < total:
#         total = sub
#         result = i
#     elif sub == total:
#         if i < result:
#             total = sub
#             result = i
        
# print(result)

# 2. 중간값 이용
result = home[(N-1)//2]
print(result)