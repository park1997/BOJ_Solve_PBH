h,m=map(int,input().split())


if 0<=m and m<45:
    if h==0:
         print(23,m+15)
    else:
        print(h-1,m+15)

elif m>=45 and m<60:
    print(h,m-45)
