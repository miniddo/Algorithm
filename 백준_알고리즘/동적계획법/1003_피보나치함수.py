import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())

    dp_zero = [0] * 41
    dp_one  = [0] * 41

    dp_zero[0], dp_one[0] = 1, 0
    dp_zero[1], dp_one[1] = 0, 1

    for i in range(2, num+1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]
    
    print(dp_zero[num], dp_one[num])

