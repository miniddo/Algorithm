from collections import deque

def solution(bridge_length, weight, truck_weights):

    wait = deque(truck_weights[1:])
    truck = deque([[truck_weights[0], 0]])
    
    time = 0
    while truck:   
        
        for t in truck:
            t[1] = t[1] + 1
        time += 1

        if truck[0][1] > bridge_length:
            truck.popleft()
        
        if len(wait) == 0:
            continue
        
        _sum = 0
        for t in truck:
            _sum += t[0]

        if len(truck) == 0 or _sum + wait[0] <= weight:
            truck.append([wait.popleft(), 1])
        else:
            continue

    return time




print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


# def solution(bridge_length, weight, truck_weights):
    
#     time = 0
#     bridge = [0] * bridge_length
    
#     while bridge:
#         time += 1
#         bridge.pop(0)
        
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 bridge.append(truck_weights.pop(0))
#             else:
#                 bridge.append(0)
    
    
#     return time