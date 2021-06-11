inStr = "파이썬 기말고사 주의사항 : 답안지 스캔 주의, 촬영 주의. 기말고사 시간 엄수. 파이썬 교재및 강의자료 답안작성 활용 가능"

file_in = open("notice.txt",mode = 'rwt',encoding='utf-8')
inStr = file_in.readlines()

print(inStr)