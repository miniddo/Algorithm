def solution(numbers):

    result = 0
    for i in range(0, 10):
        if i not in numbers:
            result += i

    return result


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 14
print(solution([5, 8, 4, 0, 6, 7, 9]))  # 6
