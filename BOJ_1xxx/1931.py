# 회의실 배정
N = int(input())
data = [list(map(int,input().split())) for i in range(N)]
data.sort(key=lambda x: (x[1],x[0]))
result = 1
s = data[0][0]
e = data[0][1]
for i in range(1,len(data)):
    if data[i][0]>=e:
        s = data[i][0]
        e = data[i][1]
        result+=1
print(result)
