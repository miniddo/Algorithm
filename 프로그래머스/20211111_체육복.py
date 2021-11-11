def solution(n, lost, reserve):

    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)

    lost.sort()
    reserve.sort()

    print(lost)
    print(reserve)

    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)

    print(lost)

    return n - len(lost)


# print(solution(5, [1, 3, 5], [2, 3, 6]))  # 5
# print(solution(1, [1], [1]))  # 1
# print(solution(5, [1, 2], [2, 3]))  # 4
# print(solution(5, [2, 3, 5], [2, 4]))  # 4
# print(solution(8, [5, 6], [4, 5]))  # 7
# print(solution(5, [2, 4], [1, 3, 5]))  # 5
# print(solution(3, [1, 2], [2, 3]))  # 2
# print(solution(3, [1, 2, 3], [1, 2, 3]))  # 3
# print(solution(5, [2, 3, 4], [3, 4, 5]))  # 4
print(solution(9, [2, 4, 7, 8], [3, 6, 9]))  # 8
