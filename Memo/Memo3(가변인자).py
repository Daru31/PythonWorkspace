# def profile(name,age,lang1,lang2,lang3,lang4,lang5): 
#     print(f'이름: {name}\t나이: {age}', end=" ") 
#     print(lang1,lang2,lang3,lang4,lang5) 
# 위 방식은 변화 가능성이 높은 변수에 대해 변수를 수정하기가 번거로움 
 
def profile(name,age,*language): 
    print(f'이름: {name}\t나이: {age}', end=" ") 
    for lang in language: 
        print(lang, end=' ') 
    print()

profile('권민석', 17, 'python', 'java', 'js', 'C', 'C++')