N = int(input())
data = [int(input()) for i in range(N)]
data.sort()
result = 0
result = data[0]*N
for i in range(1,len(data)):
    temp = data[i]*(N-i)
    if result<temp:
        result = temp
print(result)
