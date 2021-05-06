# 공유기 설치
# 이분 탐색 알고리즘
import sys
a,b=map(int,sys.stdin.readline().split())
num=[int(sys.stdin.readline()) for i in range(a)]
num.sort()
x=0
y=max(num)
while x<=y:
    distance=(x+y)//2
    count=1
    start_house=num[0]
    for j in range(1,a):
        if start_house+distance<=num[j]:
            start_house=num[j]
            count+=1
        if count>=b:
            break
    if count>=b:
        x=distance+1
        answer=distance
    elif count<b:
        y=distance-1
print(answer)