def solution(record):

    user = {}
    for r in record:
        data = r.split(' ')
        userId = data[1]
        nickName = data[2] if len(data) == 3 else ''

        if nickName != '':
            user[userId] = nickName

    answer = []
    for r in record:
        command = r.split(' ')[0]
        userId = r.split(' ')[1]
        nickName = user.get(userId)

        if command == 'Enter':
            answer.append(nickName + '님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(nickName + '님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
