# 5와 6의 차이
a=list(map(str,input().split()))
while 1:
    a[0]=a[0].replace('6','5')
    a[1]=a[1].replace('6','5')
    n1=int(a[0])+int(a[1])
    break
while 2:
    a[0]=a[0].replace('5','6')
    a[1]=a[1].replace('5','6')
    n2=int(a[0])+int(a[1])
    break
print(n1,n2)