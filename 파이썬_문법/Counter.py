from collections import Counter

arr = ['가', '가', '가', '나', '나', '나', '다', '라']
counter = Counter(arr)
print(counter) # dictionary 형태

# 유용한 method
# 1. update()
counter.update('가나')
print(counter)

# 2. elements()
print(list(counter.elements()))

# 3. most_common(n)
print(counter.most_common())
print(counter.most_common(3))

# 4. subtract()
sub = ['가', '가', '가', '나']
sub_counter = Counter(sub)
print(sub_counter)

counter.subtract(sub_counter)
print(counter)

# 연산
# 1. 덧셈
print(counter)
print(sub_counter)
print(counter + sub_counter)

# 2. 뺄셈
print(counter)
print(sub_counter)
print(counter - sub_counter)

# 3. 교집합
print(counter & sub_counter)

# 합집합
print(counter | sub_counter)