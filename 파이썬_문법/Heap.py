import heapq

# 최소 힙
def minheapsort(iterable):
  h = []
  result = []
  for i in iterable:
    heapq.heappush(h, i)
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

# 최대 힙
def maxheapsort(iterable):
  h = []
  result = []
  for i in iterable:
    heapq.heappush(h, -i)
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result1 = minheapsort([1, 3, 5, 7, 9, 4, 6, 8, 0])
result2 = maxheapsort([1, 3, 5, 7, 9, 4, 6, 8, 0])

print(result1)
print(result2)