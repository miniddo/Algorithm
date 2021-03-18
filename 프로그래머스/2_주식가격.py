def solution(prices):

    stack = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                count += 1
                break
            else:   
                count += 1

        stack.append(count)
    
    return stack


print(solution([1,2,3,2,3])) # [4, 3, 1, 1, 0]
print(solution([4,3,2,5,6])) # [1, 1, 2, 1, 0]