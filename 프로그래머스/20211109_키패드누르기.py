def solution(numbers, hand):

    left, right = '*', '#'
    result = ''

    num_dic = {0: (3, 1), 1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (
        1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), '#': (3, 2)}

    for number in numbers:
        if number in (1, 4, 7):
            result += 'L'
            left = number
        elif number in (3, 6, 9):
            result += 'R'
            right = number
        else:
            l = abs(abs(num_dic[number][0] - num_dic[left][0]) +
                    abs(num_dic[number][1] - num_dic[left][1]))
            r = abs(abs(num_dic[number][0] - num_dic[right][0]) +
                    abs(num_dic[number][1] - num_dic[right][1]))
            if l > r:
                result += 'R'
                right = number
            elif l < r:
                result += 'L'
                left = number
            else:
                if hand == 'right':
                    result += 'R'
                    right = number
                else:
                    result += 'L'
                    left = number

    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
