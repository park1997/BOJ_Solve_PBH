# 파티가 끝나고 난 뒤 
a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in c:print(i-a*b,end=" ")