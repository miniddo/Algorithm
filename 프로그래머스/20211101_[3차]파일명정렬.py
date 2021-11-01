def solution(files):

    newArr = []
    for file in files:
        head, number = file[0], ''
        point = 0
        for f in range(1, len(file)):
            pre = file[f-1] in '0123456789'
            post = file[f] in '0123456789'
            if pre == True and post == False:
                point = f
                break
            if file[f] not in '0123456789':
                head += file[f]
            else:
                if len(number) < 5:
                    number += file[f]
                else:
                    point = f
                    break

        tail = file[point:] if point != 0 else ''
        newArr.append([head, number, tail])

    newArr.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(new) for new in newArr]
    return answer


print(solution(["img12.png", "img10.png", "img02.png",
                "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
                "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png", "img2", "IMG02"]))
print(solution(["cb123345678", "db123ds12"]))
