import sys
input = sys.stdin.readline

def cutTree(M, tree):
  tree.sort()
  start, end = 1, tree[-1]
  result = 0

  while start <= end:
    mid = (start + end) // 2
    target = 0
    for t in tree:
      if t - mid >= 0:
        target += (t-mid)

    # target이 필요한 나무 길이보다 작은 경우, 더 조금씩 자른다.
    if target < M:
      end = mid - 1
    # target이 필요한 나무 길이보다 큰 경우, 더 많이씩 자른다.
    else:
      result = mid
      start = mid + 1
    
  return result

# 이진탐색의 경우, main 함수를 써야 시간초과가 안난다...!!
if __name__ == "__main__":
  N, M = map(int, input().split())
  tree = list(map(int, input().split()))
  print(cutTree(M, tree))