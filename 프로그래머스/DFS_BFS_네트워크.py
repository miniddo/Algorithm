def dfs(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if i != j and computers[i][j] == 1:
            if visited[j] == False:
                dfs(n, computers, j, visited)

def solution(n, computers):

    result = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            result += 1

    return result


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))