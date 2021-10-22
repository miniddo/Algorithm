def solution(s):

    arr = []
    for i in s:
        if not arr:
            arr.append(i)
        else:
            if arr[-1] == i:
                arr.pop()
            else:
                arr.append(i)

    if arr:
        return 1
    else:
        return 0


print(solution('baabaa'))
print(solution('cdcd'))
