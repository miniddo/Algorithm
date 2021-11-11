from itertools import combinations


def checkNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):

    answer = 0

    numList = list(combinations(nums, 3))
    for num in numList:
        if checkNum(sum(num)):
            answer += 1

    return answer


print(solution([1]))
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
