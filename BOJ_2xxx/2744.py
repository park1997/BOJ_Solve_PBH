# 대소문자 바꾸기
a=input()
b=[]
for i in a:
    if 64<ord(i)<91:
        b.append(i.lower())
    else:
        b.append(i.upper())
for i in b:
    print(i,end="")
