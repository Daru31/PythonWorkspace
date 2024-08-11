import pickle 
profile_file = open("profile.pickle", "wb") # b = binary 
profile = {"이름":"권민석", "나이":"17", "취미":"코딩"} 
print(profile) 
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장 
profile_file.close() 

profile_file = open("profile.pickle", "rb") 
profile = pickle.load(profile_file) # file 에 있는 내용을 profile 에 불러옴 
print(profile) 
profile_file.close()
