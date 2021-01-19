a=input()
cnt=0
for i in range(len(a)):
    cnt+=int(a[i])
    if int(a[i])==0:
        cnt+=int(a[i-1])*9
print(cnt)    