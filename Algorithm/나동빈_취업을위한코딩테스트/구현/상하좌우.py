r = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
s = [1,1]
n = int(input())
d = list(map(str,input().split()))
for i in d:
    print(s)
    if s[0]+r[i][0] >= 1 and s[0]+r[i][0] < n and s[1]+r[i][1] >= 1 and s[1]+r[i][1] < n:
        s[0]+=r[i][0]
        s[1]+=r[i][1]
print(*s)
