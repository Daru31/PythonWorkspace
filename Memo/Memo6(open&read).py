# 파일 읽는 법 
py = open("helloworld.py", "r", encoding="utf8") # 1st
print(py.read()) # 전체 읽기 
py.close()

py = open("helloworld.py", "r", encoding="utf8") # 2nd 
print(py.readline(), end="") # 한줄씩 읽기 후 줄바꿈 (end="" 통해 바꾸지 않음)
print(py.readline())
py.close() 

py = open("helloworld.py", "r", encoding="utf8") # 3rd 
while True: # 파일의 길이를 모를 때  
    line = py.readline() # 한줄씩 읽다가 
    if not line: 
        print("")
        break # 줄에 아무 내용이 없으면 종료 
    print(line, end="") 
py.close() 

py = open("helloworld.py", "r", encoding="utf8") # 4th 
lines = py.readlines() # 각 줄을 인자로 해서 리스트에 담아둠 
for line in lines: 
    print(line, end="") # 하나씩 빼오기 
py.close() 