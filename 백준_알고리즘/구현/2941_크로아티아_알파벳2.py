import sys
input = sys.stdin.readline

alpha = list(input().rstrip())

count = 0
while alpha:
    if len(alpha) >= 3 and alpha[0] + alpha[1] + alpha[2] == 'dz=':
        alpha = alpha[3:]
        count += 1
    elif len(alpha) >= 2 and alpha[0] + alpha[1] in ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='):
        alpha = alpha[2:]
        count += 1
    else:
        alpha = alpha[1:]
        count += 1

print(count)