# 서로 다른 L개의 알파벳 소문자
# 최소 한 개의 모음: a, e, i, o, u
# 최소 두 개의 자음
# 알파벳이 암호에서 증가하는 순서
# 조교들이 암호로 사용했을 법한 문자의 종류 C가지

import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = list(input().split())

# consonant, vowel = [], []
# for a in alpha:
#     if a == 'a' or a == 'e' or a == 'i' or a =='o' or a == 'u':
#         vowel.append(a)
#     else:
#         consonant.append(a)

# result = []
# for i in range(2, len(consonant)+1):
#     con_count, vow_count = i, L-i
#     if vow_count < 1: break
#     con_comb = list(combinations(consonant, con_count))
#     vow_comb = list(combinations(vowel, vow_count))

#     _str = ''
#     for c in con_comb:
#         for v in vow_comb:
#             _str = ''.join(c) + ''.join(v)
#             result.append(_str)

# answer = []
# for r in result:
#     newr = ''.join(sorted(list(r)))
#     answer.append(newr)

# answer = list(set(answer))
# answer.sort()

# for a in answer:
#     print(a)
    

comb = list(combinations(alpha, L))

result = []
for com in comb:
    v_num, c_num = 0, 0
    for c in com:
        if c in 'aeiou':
            v_num += 1
        else:
            c_num += 1
    if v_num >= 1 and c_num >= 2:
        value = ''.join(sorted(list(com)))
        result.append(value)

result.sort()
for r in result:
    print(r)
    
        
