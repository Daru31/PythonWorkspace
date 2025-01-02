# python 반복문을 사용해서 리스트의 각 원소에 10씩 곱하면 
data = [1,2,3,4] 
result = [] 

for i in data: 
    result.append(i*10) 

print(result)  

# numpy를 쓰면 
import numpy as np 

arr = np.array([1,2,3,4]) # numpy.ndarray 라는 type(class)으로 변환 
arr10 = arr * 10 # 원소에 10씩 알아서 곱해져요!! 

# python
print(arr10) 

price = [[100,80,70,90], [120,110,100,110]] # 2차원 데이터 
print(price[0]) # 첫번째 행을 인덱싱 
# but 특정 행을 인덱싱 할 수 없다. 

# numpy
import numpy as np 

price = [[100,80,70,90], [120,110,100,110]] # 2차원 데이터 
arr2 = np.array(price) #numpy.ndarray 타입으로 변환 
print(arr2[0, 3]) # arr2[행 번호, 열 번호] 
print(arr2[:,0]) # arr2[모든 행, 열 번호] 콜론은 '모든'을 뜻함 