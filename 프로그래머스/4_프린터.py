from collections import deque

def solution(priorities, location):

    p = []  # [[순서, 우선순위]]
    for i in range(len(priorities)):
        p.append([i, priorities[i]])
    
    prior = deque(p)
    result = []
    while prior:
        front = prior.popleft()

        flag = True
        for i in range(len(prior)):
            if front[1] < prior[i][1]:
                flag = False
                break
            else:
                continue

        if flag:
            result.append(front)
        else:
            prior.append(front)

    
    for r in range(len(result)):
        if result[r][0] == location:
            return r+1


print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5