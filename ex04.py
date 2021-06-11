while True:
    inStr = input("비밀번호를 입력하세요 : ")
    upper_Cnt, lower_Cnt, num_Cnt, etc_Cnt = [0]*4

    if len(inStr) >= 8:
        for ch in inStr:
            if ch.isupper():
                upper_Cnt +=1
                print(upper_Cnt)