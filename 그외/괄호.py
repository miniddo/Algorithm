from collections import deque

def isCollect(arr):

    stack = []
    for a in arr:
        if a == '(' or a == '[' or a == '{' or a == '<':
            stack.append(a)
        else:
            if (a == ')' or a == ']' or a == '}' or a == '>') and len(stack) == 0:
                return False
            if a == ')' and stack[-1] == '(':
                stack.pop()
            if a == ']' and stack[-1] == '[':
                stack.pop()
            if a == '}' and stack[-1] == '{':
                stack.pop()
            if a == '>' and stack[-1] == '<':
                stack.pop()

    if not stack:
        return True
    else:
        return False            



def solution(bracket):

    count = 0
    arr = deque(list(bracket))
    
    for _ in range(len(arr)):
        if arr[0] == ']' or arr[0] == '}' or arr[0] == '>' or arr[0] == ')':
            arr.append(arr.popleft())
            continue
        else:
            if isCollect(arr):
                count += 1
            arr.append(arr.popleft())

    return count




print(solution('[]{}<>()'))
print(solution('[{<>()}]'))