# 첫글자를 대문자로
a=int(input())
for i in range(a):
    b=list(map(str,input().split()))
    if 97<=ord(b[0][0]) and ord(b[0][0])<=122:
        b[0]=b[0].replace(b[0][0],chr(ord(b[0][0])-32))
    print(*b)
