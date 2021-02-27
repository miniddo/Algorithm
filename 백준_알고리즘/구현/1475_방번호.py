import sys
input = sys.stdin.readline

N = list(map(int, input().rstrip()))
arr = [[N[0]]]

for i in range(1, len(N)):
    for j in range(len(arr)):
        if N[i] == 6:
            if 9 not in arr[j] and 6 in arr[j]:
                arr[j].append(9)
                break
            elif 9 in arr[j] and 6 in arr[j]:
                if j == len(arr) - 1:
                    arr.append([N[i]])
                    break
                else:
                    continue
            else:
                arr[j].append(N[i])
                break
        elif N[i] == 9:
            if 6 not in arr[j] and 9 in arr[j]:
                arr[j].append(6)
                break
            elif 6 in arr[j] and 9 in arr[j]:
                if j == len(arr) - 1:
                    arr.append([N[i]])
                    break
                else:
                    continue
            else:
                arr[j].append(N[i])
                break
        else:
            if N[i] not in arr[j]:
                arr[j].append(N[i])
                break
            else:
                if j == len(arr) - 1:
                    arr.append([N[i]])
                    break
                else:
                    continue

print(len(arr))