# 2×n 타일링 2
a={1:1,2:3,3:5,4:11,5:21,6:43}
def f(n):
    if n in a:
        return a[n]
    else:
        a[n]=2*f(n-2)+f(n-1)
        return a[n]
print(f(int(input()))%10007)
