def solution(places):

    result = [1, 1, 1, 1, 1]
    for k in range(0, 5):
        person = []
        for i in range(0, 5):
            for j in range(0, 5):
                if places[k][i][j] == 'P':
                    person.append([i, j])

        if not person:
            continue

        for i in range(0, len(person)):
            for j in range(i+1, len(person)):
                distance = abs(person[i][0]-person[j][0]) + \
                    abs(person[i][1]-person[j][1])
                if distance == 2:
                    # print(person[i], person[j], distance)
                    if person[i][0] == person[j][0]:
                        if places[k][person[i][0]][person[i][1]+1] != 'X':
                            result[k] = 0
                    elif person[i][1] == person[j][1]:
                        if places[k][person[i][0]+1][person[i][1]] != 'X':
                            result[k] = 0
                    else:
                        if places[k][person[i][0]][person[j][1]] == 'X' and places[k][person[j][0]][person[i][1]] == 'X':
                            result[k] = 1
                        else:
                            result[k] = 0
                elif distance == 1:
                    print('히')
                    result[k] = 0

    return result


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                               "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))
