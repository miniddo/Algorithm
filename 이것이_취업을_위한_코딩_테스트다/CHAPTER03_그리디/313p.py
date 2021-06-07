import sys
input = sys.stdin.readline

s = list(map(int, input().rstrip()))
zero, one, count = 0, 0, 1

for i in range(len(s)-1):
    if s[i] == s[i+1]: 
        count += 1
    else:
        if s[i] == 0: zero += 1
        elif s[i] == 1: one += 1
        count = 1
    
    if i == len(s)-2:
        if s[i] == s[i+1]:
            if s[i] == 0: zero += 1
            elif s[i] == 1: one += 1
        else:
            zero += 1
            one += 1

if zero < one: print(zero)
else: print(one)