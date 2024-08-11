# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 추첨 프로그램을 작성하시오. 

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정 
# 조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가 
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용 

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

from random import *

users = range(1, 21)
users = list(users)

winners = sample(users, 4)
# previous :
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ") 

# with f strings (After I learned about 'sorting formatted output' ) :
print(f"{" 당첨자 발표 ":-^12}") # 반복되는 문자가 이거보다 많을 때 유용할 듯 
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")
print(f"{" 축하합니다 ":-^11}") 
