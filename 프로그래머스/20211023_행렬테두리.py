def solution(rows, columns, queries):

    # 배열 만들기
    matrix = []
    for i in range(1, rows+1):
        subMatrix = []
        for j in range(1, columns+1):
            subMatrix.append((i-1)*columns+j)
        matrix.append(subMatrix)

    # 바꿀 값 배열에 넣기
    result = []
    for querie in queries:
        rotate = []
        startX, startY = querie[0] - 1, querie[1]-1
        endX, endY = querie[2]-1, querie[3]-1
        x, y = startX, startY
        indexMatrix = []
        while y <= endY:
            rotate.append(matrix[x][y])
            indexMatrix.append([x, y])
            y += 1
        x += 1
        y -= 1
        while x <= endX:
            rotate.append(matrix[x][y])
            indexMatrix.append([x, y])
            x += 1
        x -= 1
        y -= 1
        while y >= startY:
            rotate.append(matrix[x][y])
            indexMatrix.append([x, y])
            y -= 1
        x -= 1
        y += 1
        while x > startX:
            rotate.append(matrix[x][y])
            indexMatrix.append([x, y])
            x -= 1

        rotate.insert(0, rotate.pop())
        for i in range(0, len(rotate)):
            xx, yy = indexMatrix[i][0], indexMatrix[i][1]
            matrix[xx][yy] = rotate[i]

        result.append(min(rotate))

    return result


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
