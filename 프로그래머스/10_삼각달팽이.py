def solution(n):

    triangle = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            if i % 3 == 1:
                y += 1
            if i % 3 == 2:
                x -= 1
                y -= 1

            triangle[x][y] = num
            num += 1
    
    result = []
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if triangle[i][j] != 0:
                result.append(triangle[i][j])
    
    return result
    

print(solution(4))
print(solution(5))
print(solution(6))