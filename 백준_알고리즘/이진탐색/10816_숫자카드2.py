import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))

count = Counter(NList)
for i in MList:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ') 

# NCount = list(Counter(NList).items())
# NCount.sort(key=lambda x:x[0])

# result = []
# for i in range(M):
#     start, end = 0, len(NCount)-1
#     target = MList[i]
#     flag = False
#     while start <= end:
#         mid = (start + end)//2
#         if target == NCount[mid][0]:
#             result.append(NCount[mid][1])
#             flag = True
#             break
#         elif NCount[mid][0] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     if flag == False:
#         result.append(0)

# for r in result:
#     print(r, end=' ')