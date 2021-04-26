def solution(info, query):
    
    infoArr = []
    for i in info:
        infoArr.append(i.split(' '))
    
    queryArr = []
    for q in query:
        queryArr.append(q.split(' and '))
    
    for q in range(len(queryArr)):
        food, score = queryArr[q][-1].split(' ')
        del queryArr[q][-1]
        queryArr[q].extend([food, score])
    
    result = []
    for i in queryArr:
        count = 0
        for j in infoArr:
            if (i[0] == '-' or i[0] == j[0]) and (i[1] == '-' or i[1] == j[1]) and (i[2] == '-' or i[2] == j[2]) and (i[3] == '-' or i[3] == j[3]) and int(i[4]) <= int(j[4]):
                count += 1
        
        result.append(count)
    
    return result
                