num=[list(map(int,input().split())) for i in range(int(input()))]
num.append([num[0][0],num[0][1]])
x,y=0,0
for i in range(len(num)-1):
    x+=num[i][0]*num[i+1][1]
    y+=num[i][1]*num[i+1][0]
print(round(abs(x-y)/2,2))
