# 시험점수
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(sum(b))
else:
    print(sum(a))