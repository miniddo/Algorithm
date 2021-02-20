import sys
input = sys.stdin.readline

one = list(map(int, input().rstrip()))
two = list(map(int, input().rstrip()))
three = list(map(int, input().rstrip()))
four = list(map(int, input().rstrip()))
K = int(input()) # 회전횟수
rule = [list(map(int, input().split())) for _ in range(K)]

def rotateGear(count, gear):
    if count == 1:
        gear.insert(0, gear.pop())
    elif count == -1:
        gear.append(gear.pop(0))

for i in rule:

    count1, count2, count3, count4 = 0, 0, 0, 0

    # 처음으로 회전시킨 톱니바퀴에 따라 경우 나누기
    if i[0] == 1:
        if i[1] == 1: # 시계방향
            count1 += 1
            if one[2] == two[6]: count2 = 0
            else: count2 -= 1
        elif i[1] == -1: # 반시계방향
            count1 -= 1
            if one[2] == two[6]: count2 = 0
            else: count2 += 1
        
        if count2 == 1:
            if two[2] == three[6]: count3 = 0
            else: count3 -= 1
        elif count2 == -1:
            if two[2] == three[6]: count3 = 0
            else: count3 += 1
        elif count2 == 0:   count3 = 0

        if count3 == 1:
            if three[2] == four[6]: count4 = 0
            else: count4 = -1
        elif count3 == -1:
            if three[2] == four[6]: count4 = 0
            else: count4 += 1
        elif count3 == 0:   count4 = 0

    elif i[0] == 2:
        if i[1] == 1:
            count2 += 1
            if one[2] == two[6]:   count1 = 0
            else: count1 -= 1

            if two[2] == three[6]: count3 = 0
            else: count3 -= 1
        elif i[1] == -1:
            count2 -= 1
            if one[2] == two[6]:   count1 = 0
            else: count1 += 1

            if two[2] == three[6]: count3 = 0
            else: count3 += 1
        
        if count3 == 1:
            if three[2] == four[6]: count4 = 0
            else: count4 = -1
        elif count3 == -1:
            if three[2] == four[6]: count4 = 0
            else: count4 += 1
        elif count3 == 0:   count4 = 0

    elif i[0] == 3:
        if i[1] == 1:
            count3 += 1
            if two[2] == three[6]: count2 = 0
            else: count2 -= 1

            if three[2] == four[6]: count4 = 0
            else: count4 -= 1
        
        elif i[1] == -1:
            count3 -= 1
            if two[2] == three[6]: count2 = 0
            else: count2 += 1

            if three[2] == four[6]: count4 = 0
            else: count4 += 1
        
        if count2 == 1:
            if one[2] == two[6]: count1 = 0
            else: count1 -= 1
        elif count2 == -1:
            if one[2] == two[6]: count1 = 0
            else: count1 +=1
        elif count2 == 0:   count1 = 0

    elif i[0] == 4:
        if i[1] == 1:
            count4 += 1
            if three[2] == four[6]: count3 = 0
            else: count3 -= 1
        elif i[1] == -1:
            count4 -= 1
            if three[2] == four[6]: count3 = 0
            else: count3 += 1
        
        if count3 == 1:
            if two[2] == three[6]: count2 = 0
            else: count2 -= 1
        elif count3 == -1:
            if two[2] == three[6]: count2 = 0
            else: count2 += 1
        elif count3 == 0:   count2 = 0

        if count2 == 1:
            if one[2] == two[6]: count1 = 0
            else: count1 = -1
        elif count2 == -1:
            if one[2] == two[6]: count1 = 0
            else: count1 += 1
        elif count2 == 0:   count1 = 0
    
    # 회전 시키기
    rotateGear(count1, one)
    rotateGear(count2, two)
    rotateGear(count3, three)
    rotateGear(count4, four)


# 점수 계산하기
result = 0
if one[0] == 1:     result += 1
if two[0] == 1:     result += 2
if three[0] == 1:   result += 4
if four[0] == 1:    result += 8

print(result)