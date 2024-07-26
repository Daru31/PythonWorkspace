# def profile(name,age,lang1,lang2,lang3,lang4,lang5): 
#     print(f'이름: {name}\t나이: {age}', end=" ") 
#     print(lang1,lang2,lang3,lang4,lang5) 
# 위 방식은 변화 가능성이 높은 변수에 대해 변수를 
# 수정하기가 번거롭고, 변수 개수를 문장마다 다르게 사용할 때 
# 변수를 적게 쓰는 경우에는 따로 공백을 만들어서 변수 개수를 
# 맞춰야 하는 번거로움이 있음. 
 
def profile(name,age,*language): # 가변인자 *
    print(f'이름: {name}\t나이: {age}', end=" ") 
    for lang in language: # for 문 사용해서 출력
        print(lang, end=' ') 
    print()

profile('권민석', 17, 'python', 'java', 'js', 'C', 'C++') 
profile('지한서', 17, 'python') 
# 정의한 함수 하나로 변수 개수가 다르게 출력 가능