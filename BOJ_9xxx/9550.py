# 아이들은 사탕을 좋아해 
for i in range(int(input())):
    cnt=0
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for j in range(len(c)):
        cnt+=c[j]//b
    print(cnt)