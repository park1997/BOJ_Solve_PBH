# 정수삼각형
a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
result=b
for i in range(1,a):
    for j in range(len(b[i])):
        if j==0:
            result[i][j]=b[i][j]+result[i-1][j]
        elif j==i:
            result[i][j]=b[i][j]+result[i-1][j-1]
        else:
            result[i][j]=b[i][j]+max(result[i-1][j-1],result[i-1][j])

print(max(result[-1]))
