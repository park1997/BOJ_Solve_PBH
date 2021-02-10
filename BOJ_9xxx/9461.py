# 파도반 수열
memo={1:1,2:1,3:1,4:2,5:2}
def f(n):
    if n in memo:
        return(memo[n])
    else:
        memo[n]=f(n-1)+f(n-5)
        return memo[n]
a=int(input())
for i in range(a):
    print(f(int(input())))
    