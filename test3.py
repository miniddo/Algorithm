import re

value = 'AAAAA'
count = 0
while True:
    k = value.replace('AA', '', 1)
    print(k)
    if value != k:
        count += 1
        value = k
    else:
        break

print(value)
print(count)
