def solution(cacheSize, cities):

    cache = []
    time = 0

    if cacheSize == 0:
        return len(cities) * 5

    for citie in cities:
        citie = citie.lower()
        if len(cache) < cacheSize:
            if citie not in cache:
                cache.append(citie)
                time += 5
            else:
                cache.remove(citie)
                cache.append(citie)
                time += 1
        else:
            if citie in cache:
                cache.remove(citie)
                cache.append(citie)
                time += 1
            else:
                del cache[0]
                cache.append(citie)
                time += 5

    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
                   "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
                   "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                   "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5, ["Seoul", "Seoul", "Seoul"]))
