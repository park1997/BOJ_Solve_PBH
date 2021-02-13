# 문자열 분석
while 1:
    l=0
    s=0
    sp=0
    num=0
    try:
        a=input()
        for i in a:
            if i==" ":
                sp+=1
            elif 64<ord(i)<91:
                l+=1
            elif 96<ord(i)<123:
                s+=1
            else:
                num+=1
        print("{} {} {} {}".format(s,l,num,sp))

    except EOFError:
        break


