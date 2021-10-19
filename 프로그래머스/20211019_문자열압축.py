def solution(s):

    compressionLength = len(s) // 2
    result = len(s)

    for i in range(1, compressionLength+1):
        sliceArr = []
        repeat = len(s)//i if len(s) % i == 0 else len(s)//i+1
        for j in range(0, repeat):
            sliceArr.append(s[j*i:j*i+i])

        count = 1
        resultStr = ''
        for k in range(0, len(sliceArr)-1):
            if sliceArr[k] == sliceArr[k+1]:
                count += 1
            else:
                addCount = '' if count == 1 else str(count)
                resultStr += (addCount + sliceArr[k])
                count = 1

        _addCount = '' if count == 1 else str(count)
        if sliceArr[-2] == sliceArr[-1]:
            resultStr += (_addCount + sliceArr[-1])
        else:
            resultStr += sliceArr[-1]

        if len(resultStr) < result:
            result = len(resultStr)

    return result


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
