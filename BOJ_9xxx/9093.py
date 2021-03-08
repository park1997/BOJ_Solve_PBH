# 단어 뒤집기
a=int(input())
b=[list(map(str,input().split())) for i in range(a)]
result_1=[]
for i in b:
    result=[]
    for j in i:
        result.append(j[::-1])
    result_1.append(result)
for i in result_1:
    print(*i)