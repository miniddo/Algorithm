def treeSort(wordSort, wordSet):
    
    dic = {}
    for w in wordSet:
        dic[w[0]] = [w[1], w[2]]
    
    result = []
    for w in wordSort:
        if len(w) == 3:
            node = dic[w[0]]
        else:
            node = dic[w[0][0]]
        sub = []
        while True:
            sub.append(node[0])
            if node[1] != '0':
                node = dic[node[1]]
            else: break
        sub.reverse()
        result.append('/'.join(sub))
    
    return result


def solution(data, word):

    wordSet = []
    for d in data:
        temp = d.split()
        wordSet.append([temp[0], temp[1], temp[2]])
    
    wordSelect = []
    for w in wordSet:
        if word in w[1] and w[2] != '0':
            wordSelect.append(w)
    
    wordSort = []
    # 1. 정확히 일치하는 인형 검색
    for w in wordSelect:
        if w[1] == word:
            wordSort.append(w)
            wordSelect.remove(w)
    
    sub = []
    for w in wordSelect:
        # 2. word가 많이 포함될수록 먼저 검색
        value = w[1]
        count = 0
        while True:
            k = value.replace(word, '', 1)
            if value != k:
                count += 1
                value = k
            else: break
        
        # 2-1. word가 앞에 있을 수록 먼저 검색
        one = w[1].find(word)
        # 2-2. word 위치 같다면, 다음 word 위치 비교
        two = w[1].find(word, one+len(word))
        # 2-3. ID가 더 작은 인형을 먼저 나열
        three = int(w[0])

        sub.append([w, count, one, two, three])
    
    sub.sort(key=lambda x:(-x[1],x[2],x[3],x[4]))
    wordSort.extend(sub)

    if not wordSort:
        return ["Your search for (" + word + ") didn't return any results"]

    result = treeSort(wordSort, wordSet)
    return result
        



print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"], "BROWN"))
print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"], "SALLY"))
print(solution(["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"], "AA"))