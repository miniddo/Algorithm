import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

# 책과 비교

# 내 코드
# 문제점: 이미 sort를 해놓은 상태이기 때문에 index로만 비교하면 된다.
# 내장함수 sum을 쓰는 것에서 이미 효율성이 떨어질 수 있다.
max_sum = sum(A)
for i in range(K):
    A[i], B[i] = B[i], A[i]
    if sum(A) > max_sum:
        max_sum = sum(A)

print(max_sum)