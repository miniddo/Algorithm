def fibo(x):
    if x < 2:
        return x
    else: 
        return fibo(x-1) + fibo(x-2)


print(fibo(10))

'''
피보나치 수열의 가장 기본적인 풀이!
but, 시간복잡도는 수의 크기가 커질 수록 커진다 => O(n^2)
'''