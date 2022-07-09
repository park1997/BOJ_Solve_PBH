# 패션왕 신해빈
N = int(input())
for _ in range(N):
    type = {}
    cloth = []
    n = int(input())
    for i in range(n):
        c,t = map(str,input().split())
        if t not in type:
            type[t] = [c]
        else:
            type[t].append(c)
    result = 1
    for j in type:
        type[j] = set(type[j])
        result*=(len(type[j])+1)
    if n==0:
        print(0)
    else:
        print(result-1)