class Unit: # Unit 이라는 이름의 "객체"
    def __init__(self, name, hp, damage): # __init__ : 파이썬 내에서의 생성자 = 이걸 사용한 클래스는 변수에 할당만 해줘도 호출됨
        self.name = name
        self.hp = hp 
        self.damage = damage 
        print(f"{self.name} 유닛이 생성되었습니다.\n체력 : {self.hp}, 공격력 : {self.damage}") 
          
marine1 = Unit("마린", 40, 5) # Unit 객체의 "인스턴스" -> class 내 함수에 저장됨! 
marine2 = Unit("마린", 40, 5) # ``
tank = Unit("탱크", 150, 35) # `` 
print(f"유닛 이름 : {tank.name}, 공격력 : {tank.damage}") # 멤버변수(class 내 함수에 저장한 변수)는 class 외부에서도 호출 가능! 

wraith1 = Unit("레이스", 80, 5) 
wraith1.clocking = True # 멤버변수가 아니지만, class 외부에서 변수 생성이 가능함. 

if wraith1.clocking == True: 
    print(f"{wraith1.name}는 현재 클로킹 상태입니다. ")