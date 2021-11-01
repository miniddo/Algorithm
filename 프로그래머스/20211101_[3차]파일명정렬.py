def solution(files):

    newArr = []
    for file in files:
        str, number = '', ''
        for f in file:
            if f not in '0123456789':
                str += f
            else:
                if len(number) < 5:
                    number += f
                else:
                    str += f

        start = file.index(number)
        end = len(number)

        head = file[0:start]
        tail = file[start+end:]

        print(number)
        newArr.append([head, number, tail])

    newArr.sort(key=lambda x: (x[0].lower(), int(x[1])))

    answer = [''.join(new) for new in newArr]
    return answer


# print(solution(["img12.png", "img10.png", "img02.png",
#                 "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
#                 "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png", "img2", "IMG02"]))
# ["img1.png","img2","IMG02", "img000012345"]
