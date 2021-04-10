def divide(p):

    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            return u, v

def isCollect(u):
    
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
        return True


def solution(p):

    if p == '':
        return ''

    # 2
    u, v = divide(p)
    
    # 3
    if isCollect(u):
        return u + solution(v)
    # 4
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = u[1:len(u)-1]
        for i in u:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result



print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))