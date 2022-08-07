# 시험감독
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
result = 0
for a in A:
    temp = a - B
    result += 1
    if temp > 0:
        if temp%C==0:
            result += temp//C
        else:
            result += temp//C + 1
print(result)