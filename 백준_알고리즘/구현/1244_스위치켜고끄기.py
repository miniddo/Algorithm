import sys
input = sys.stdin.readline

S = int(input())
switch = list(map(int, input().split()))
N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]

# print(switch)

for i in student:
  if i[0] == 1: # 남자
    for j in range(S):
      if (j+1) % i[1] == 0:  # 스위치 번호가 배수이면, 상태 바꾸기
        if(switch[j] == 0): switch[j] = 1
        else: switch[j] = 0
        
  else: # 여자
    # print('여자')
    # print('여자가 받은 수: ', j[1])
    # print('스위치의 위치: ', j[1]-1)
    # print('스위치 상태: ', switch[j[1]-1])

    location = j[1] - 1
    if switch[location] == 0: switch[location] = 1
    else: switch[location] = 0

    left, right = location - 1, location + 1
    flag = True

    while flag:
      if left < 0 or right > len(switch) - 1:
        flag = False
      
      if left == right:
        if switch[left] == 0: switch[left] = 1
        else: switch[left] = 0

        if switch[right] == 0: switch[right] = 1
        else: switch[right] = 0

        left -= 1
        right += 1
      else:
        flag = False

  # print(switch)