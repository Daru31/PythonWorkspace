gun = 10 # 지역 변수
def checkpoint(soldiers): 
    global gun # 전역 변수로 설정 -> 관리가 어려워지므로 권장 X
    gun = gun - soldiers 
    print(f'[함수 내] 남은 총 : {gun}') 

def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers # 10 = 10 - soldiers
    print(f'[함수 내] 남은 총 : {gun}') # 10 - soldiers
    return gun # 함수를 호출할 때 지금 계산된 값을 받을 수 있도록 

print(f'전체 총 수 : {gun}') # 1번 줄 gun = 10 
gun = checkpoint_ret(gun, 2) # 함수 계산 후 나온 리턴값 gun 
print(f'남은 총 : {gun}') # 10 - 2 = 8