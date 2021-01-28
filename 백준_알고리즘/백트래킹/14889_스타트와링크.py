import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
person = [i+1 for i in range(N)]
power = [list(map(int, input().split())) for _ in range(N)]

team = list(combinations(range(1,N+1), N//2))
start_team, link_team = 0, 0

count = 0  
for start in team:
    # 상대편 구하기
    start = set(start)
    link = set(person) - start

    # 각 팀 조합하기
    s = list(combinations(start, 2))
    l = list(combinations(link, 2))

    start_power, link_power = 0, 0
    for ss in s:
        start_power += power[ss[0]-1][ss[1]-1] + power[ss[1]-1][ss[0]-1]
    for ll in l:
        link_power += power[ll[0]-1][ll[1]-1] + power[ll[1]-1][ll[0]-1]
    
    if count == 0:
        start_team = start_power
        link_team = link_power
    else:
        if abs(start_power - link_power) < abs(start_team - link_team):
            start_team = start_power
            link_team = link_power
    
    count += 1

print(abs(start_team - link_team))

