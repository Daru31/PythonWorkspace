customer = "토르"
person = ()

while person != customer : 
    print("{}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    if person == customer : 
        print("커피 여기있습니다.")