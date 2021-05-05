import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(2, N+1)]
result = []

while True:
    arr.sort()
    k = 0
    flag = True
    while flag:
        P = arr[k]
        for i in range(2, P):
            if P % i == 0:
               k += 1
               break
        flag = False
    p = arr[k]
    arr.remove(p)
    result.append(p)

    for a in arr[:]:
        if a % p == 0:
            arr.remove(a)
            result.append(a)
    
    if not arr: break


print(result[K-1])
    

