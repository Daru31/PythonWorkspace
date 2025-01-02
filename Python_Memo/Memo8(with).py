with open("python.txt", "w", encoding="utf8") as python_file: 
    python_file.write("파이썬") 

with open("python.txt", "r", encoding="utf8") as python_read_file: 
    print(python_read_file.read()) 

# 훨씬 간단하게 파일을 쓰고 읽을 수 있다. 