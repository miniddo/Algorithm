def solution1(s):

    if 'zero' in s:
        s = s.replace('zero', '0')
    if 'one' in s:
        s = s.replace('one', '1')
    if 'two' in s:
        s = s.replace('two', '2')
    if 'three' in s:
        s = s.replace('three', '3')
    if 'four' in s:
        s = s.replace('four', '4')
    if 'five' in s:
        s = s.replace('five', '5')
    if 'six' in s:
        s = s.replace('six', '6')
    if 'seven' in s:
        s = s.replace('seven', '7')
    if 'eight' in s:
        s = s.replace('eight', '8')
    if 'nine' in s:
        s = s.replace('nine', '9')

    return int(s)


def solution2(s):

    number = [
        ('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    ]

    for num in number:
        if num[0] in s:
            s = s.replace(num[0], num[1])

    return int(s)


def solution(s):

    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for key, value in num_dic.items():
        s = s.replace(key, value)

    return int(s)


print(solution('one4seveneight'))  # 1478
print(solution('23four5six7'))  # 234567
print(solution('2three45sixseven'))  # 234567
print(solution('123'))  # 123
