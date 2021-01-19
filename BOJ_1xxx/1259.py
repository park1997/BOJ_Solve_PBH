# 펠린드롬수
while 1:
    a=input()
    if a=='0':
        break
    if a==a[::-1]:
        print('yes')
    else:
        print('no')