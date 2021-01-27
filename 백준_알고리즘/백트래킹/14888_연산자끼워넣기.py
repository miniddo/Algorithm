# 연산자의 모든 경우의 수 구하기
# 중복 제거하기
# 순서 상관 있음 => permutations

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())    # 수의 개수
AList = list(map(int, input().split()))     # 수
calculate = list(map(int, input().split())) # 연산자

plus    = ['+'] * calculate[0]
minus   = ['-'] * calculate[1]
multi   = ['*'] * calculate[2]
divide  = ['//'] * calculate[3]

CList = plus + minus + multi + divide

permu = list(permutations(CList, len(CList))) # 연산자의 모든 경우의 수 구하기
permu = list(set(permu))    # 중복제거

result = []         # 모든 연산


for i in range(len(permu)):
    value = AList[0]    # 수의 첫번째는 넣고 시작
    for j in range(len(permu[i])):
        if permu[i][j] == '+':
            value += AList[j+1]
        elif permu[i][j] == '-':
            value -= AList[j+1] 
        elif permu[i][j] == '*':
            value *= AList[j+1]
        elif permu[i][j] == '//':
            if(value < 0 and AList[j+1] > 0):
                value = -(abs(value) // AList[j+1])
            else:
                value //= AList[j+1]
    result.append(value)

result.sort()
print(result[-1])   # 최댓값
print(result[0])    # 최솟값

