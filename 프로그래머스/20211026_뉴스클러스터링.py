def solution(str1, str2):

    str1, str2 = str1.upper(), str2.upper()

    arr1 = [str1[s:s+2] for s in range(0, len(str1)-1)]
    arr2 = [str2[s:s+2] for s in range(0, len(str2)-1)]

    arr1 = list(filter(lambda x: (x[0].isalpha() and x[1].isalpha()), arr1))
    arr2 = list(filter(lambda x: (x[0].isalpha() and x[1].isalpha()), arr2))

    set1, set2 = set(arr1), set(arr2)
    union = list(set1 | set2)
    intersection = list(set1 & set2)

    count1, count2 = 0, 0
    for u in union:
        count1 += max(arr1.count(u), arr2.count(u))
    for i in intersection:
        count2 += min(arr1.count(i), arr2.count(i))

    if count1 == 0:
        return 65536
    else:
        return int(count2/count1*65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
