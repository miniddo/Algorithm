import sys
import math
input = sys.stdin.readline

N = input().rstrip()
count = [0] * 9

for num in N:
    if num == '6' or num == '9':
        count[6] += 1
    else:
        count[int(num)] += 1
    
maxN = max(count)
if maxN == count[6]:
    count[6] = math.ceil(maxN/2)
maxN = max(count)

print(maxN)