absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        print("{0}번은 오늘 학교를 안왔구나.".format(student))
        continue
    elif student in no_book:
        print("책을 안 가지고 오다니, {0}번은 교무실로 따라와.".format(student))
        break
    print("{0}번, 책을 읽어봐.".format(student))