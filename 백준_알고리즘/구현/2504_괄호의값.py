import sys
_str = input().rstrip()

def checkStr(bs): 
    stack = [] 
    for b in bs: 
        if b == '(' or b =='[': 
            stack.append(b) 
        elif b == ')' and stack: 
            if stack[-1] == '(': 
                stack.pop() 
            else: stack.append(b) 
        elif b ==']' and stack: 
            if stack[-1] == '[': 
                stack.pop() 
            else: stack.append(b) 
        else: 
            stack.append(b) 
    
    if stack: return False 
    else: return True 


def solution(_str):
    stack = []
    for s in _str:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                val = 0
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = val * 2
                        break
                    else:
                        val += stack[i]
                        stack.pop()
        if s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                val = 0
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = val * 3
                        break
                    else:
                        val += stack[i]
                        stack.pop()

    return sum(stack)

if checkStr(_str):
    print(solution(_str))
else:
    print(0) 