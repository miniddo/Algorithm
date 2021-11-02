def solution(new_id):
    new_id = list(new_id)

    # 1단계
    for idx in range(0, len(new_id)):
        if new_id[idx].isalpha():
            new_id[idx] = new_id[idx].lower()

    # 2단계
    for id in new_id[:]:
        if id not in 'abcdefghijklnmopqrstuvwxyz0123456789-_.':
            new_id.remove(id)

    # 3단계
    new_id = ''.join(new_id)
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
            continue
        else:
            break

    # 4단계
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while True:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("z-+.^."))  # "z--"
print(solution("=.="))  # "aaa"
print(solution("123_.def"))  # "123_.def"
print(solution("abcdefghijklmn.p"))  # "abcdefghijklmn"
