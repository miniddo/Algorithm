import sys
from collections import deque
input = sys.stdin.readline

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha = list(input().rstrip())
q = deque(alpha)

count = 0
while q:
    if len(q) >= 2 and q[0] + q[1] in arr:
        q.popleft()
        q.popleft()
        count += 1
        continue
    elif  len(q) >= 3 and q[0] + q[1] + q[2] in arr:
        q.popleft()
        q.popleft()
        q.popleft()
        count += 1
        continue
    else:
        q.popleft()
        count += 1

print(count)