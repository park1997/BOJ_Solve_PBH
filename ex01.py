a,b=map(str,input().split())
result=''
if len(a)==len(b):
    for i in range(len(a)):
        result+=str((int(a[i])+int(b[i])))
elif len(a) < len(b):
    result+=b[0:len(b)-len(a)]
    for i in range(len(a)):
        result+=str(int(a[i])+int(b[i+(len(b)-len(a))]))
elif len(a) > len(b):
    result+=a[0:len(a)-len(b)]
    for i in range(len(b)):
        result+=str(int(b[i])+int(a[i+(len(a)-len(b))]))
print(result)