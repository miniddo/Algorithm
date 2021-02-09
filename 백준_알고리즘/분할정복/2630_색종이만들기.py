import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
w_paper, b_paper = 0, 0

def countPaper(x, y, n):
  global w_paper, b_paper   # 함수 안에서 외부 값 사용할 때는 global 변수
  color = paper[x][y]       # 현재 위치의 색 구하기

  # 해당 구역해서 하나라도 다른 색이 있으면 사분면을 나눈다.
  for i in range(x, x+n):
    for j in range(y, y+n):
      if paper[i][j] != color:
        countPaper(x, y, n//2)
        countPaper(x+n//2, y, n//2)
        countPaper(x, y+n//2, n//2)
        countPaper(x+n//2, y+n//2, n//2)
        return
  
  if color == 0:
    w_paper += 1
  else:
    b_paper += 1
    
countPaper(0, 0, N)
print(w_paper)
print(b_paper)



'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
'''