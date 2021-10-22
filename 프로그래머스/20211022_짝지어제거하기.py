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
        return 0
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))
