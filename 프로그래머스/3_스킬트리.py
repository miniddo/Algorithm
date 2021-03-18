def solution(skill, skill_trees):

    skill = list(skill)
    count = 0

    for alpha in skill_trees:
        stack = []
        for a in alpha:
            if a in skill: stack.append(a)
        
        flag = True
        for i in range(len(stack)):
            if skill[i] != stack[i]:
                flag = False
                break
        
        if flag:
            count += 1
    
    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))   # 2