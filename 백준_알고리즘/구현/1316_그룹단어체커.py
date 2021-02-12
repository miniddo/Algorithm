import sys
input = sys.stdin.readline

result = []

def checkGroup(name):

    global result
    
    flag = True
    dic = {}
    for i in range(len(name)):
        if i == 0:
            dic[name[i]] = 1
        else:
            if name[i] != name[i-1] and dic.get(name[i], 0) == 0:
                dic[name[i]] = 1
                continue
            elif name[i] == name[i-1] and dic.get(name[i], 0) == 1:
                continue
            elif name[i] != name[i-1] and dic.get(name[i], 0) == 1:
                flag = False
                break
    
    if flag == True:
        result.append(name)

N = int(input())
for _ in range(N):
    checkGroup(input().rstrip())

print(len(result))