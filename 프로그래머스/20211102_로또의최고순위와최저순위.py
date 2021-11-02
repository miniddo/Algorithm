def matchScore(index, score, result):
    if score == 6:
        result[index] = 1
    elif score == 5:
        result[index] = 2
    elif score == 4:
        result[index] = 3
    elif score == 3:
        result[index] = 4
    elif score == 2:
        result[index] = 5
    else:
        result[index] = 6


def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    lowest = 0
    for l in lottos:
        if l in win_nums:
            lowest += 1

    highest = lowest + lottos.count(0)

    return [rank[highest], rank[lowest]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]

# 1위 - 6
# 2위 - 5
# 3위 - 4
# 4위 - 3
# 5위 - 2
# 6위 - 그외
