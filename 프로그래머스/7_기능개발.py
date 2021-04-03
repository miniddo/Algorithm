from collections import deque
import math

def solution(progresses, speeds):

    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    day = deque(days)

    result, sub = [], []
    while True:

        if not day:
            result.append(len(sub))
            sub.clear() 
            break

        if not sub:
            sub.append(day.popleft())
            continue

        if sub[0] < day[0]:
            result.append(len(sub))
            sub.clear()
        else:
            sub.append(day.popleft())


    return result


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]