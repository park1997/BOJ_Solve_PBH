#방학숙제
a=[int(input()) for i in range(5)]
if a[1]%a[3]==0:
    b=a[1]//a[3]
else:
    b=(a[1]//a[3])+1
if a[2]%a[4]==0:
    c=(a[2]//a[4])
else:
    c=(a[2]//a[4])+1
if b>=c:
    print(a[0]-b)
else:
    print(a[0]-c)
