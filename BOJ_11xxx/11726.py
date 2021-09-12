# 2xn 타일링
a={1:1,2:2}
def f(n):
    if n in a:
        return a[n]
    else:
        a[n]=f(n-2)+f(n-1)
        return a[n]
print(f(int(input()))%10007)
