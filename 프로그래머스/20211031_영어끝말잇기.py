def solution(n, words):

    used = []
    count = 0
    while True:
        if len(words) == 0:
            break
        count += 1
        for i in range(1, n+1):
            word = words.pop(0)
            if len(used) == 0:
                used.append(word)
            else:
                if word in used or used[-1][-1] != word[0]:
                    return [i, count]
                else:
                    used.append(word)

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
                   "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                   "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# [번호, 차례]
# [3, 3]
# [0, 0]
# [1, 3]
