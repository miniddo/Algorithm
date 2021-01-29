import sys
from collections import Counter

input = sys.stdin.readline
nameList = list(input().rstrip())
nameList = list(Counter(nameList).items())
nameList.sort(key=lambda x:x[0])

even, odd = [], []      # even: 짝수, odd: 홀수
for n in nameList:
    if n[1] % 2 == 0: even.append(n)
    else: odd.append(n)

result = ''
if len(odd) == 0: # 모든 알파벳이 짝수개
    for e in even:
        result += (e[0] * (e[1] // 2))
    result += result[::-1]
    print(result)
elif len(odd) == 1: # 한 알파벳만 홀수개
    oddEven = even + odd
    oddEven.sort(key=lambda x:x[0])
    for o in oddEven:
        if o[1] % 2 == 0:
            result += (o[0] * (o[1] // 2))
        else:
            result += (o[0] * ((o[1]-1) // 2))
    print(result + odd[0][0] + result[::-1])
else:
    print("I'm Sorry Hansoo")