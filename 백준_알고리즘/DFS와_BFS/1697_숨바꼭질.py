import sys
from collections import deque
input = sys.stdin.readline

def bfs():

    location = [0] * 100001
    queue = deque([])
    queue.append(N)

    while queue:
        x = queue.popleft()

        if x == K:
            return location[x]
        
        sub = [x+1, x-1, x*2]

        for s in sub:
            if s >= 0 and s <= 100000 and location[s] == 0:
                location[s] = location[x]+1
                queue.append(s)

N, K = map(int, input().split())
print(bfs())