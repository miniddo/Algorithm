# 섞은 음식의 스코빌 지수 
# = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):

    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
            answer += 1
        except IndexError:
            return -1
    
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
