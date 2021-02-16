d = [0] * 100

def fibo(x):
    if x < 2:
        return x
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


print(fibo(10))

'''
다이나믹 프로그래밍으로 푼 피보나치 수열

재귀함수를 이용하는 방법은 '탑다운(Top-Down) 방식'
메모이제이션(Memoization)을 이용한다.

한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면
메모한 결과를 그대로 가져오는 기법이다.
'''