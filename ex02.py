from collections import deque
def check_index(x,y):
    try:
        if miro[y][x]==1:
            return True
        else:
            return False
    except :
        return False
N,M = map(int,input().split())
miro = []
result=[]
for i in range(N):
    temp=[]
    temp0=[]
    for j in input():
        temp.append(int(j))
        temp0.append(0)
    miro.append(temp)
    result.append(temp0)

q = deque()
x,y=0,0
result[y][x]=1
prev_x,prev_y=-1,-1
cnt=1
q.append([x,y])
while 1 :
    print(q)
    for x,y in q:
        result[y][x]=cnt
    for i in range(len(q)):
        x,y=q.popleft()
        if check_index(x+1,y):
            q.append([x+1,y])
        if check_index(x,y+1):
            q.append([x,y+1])
        if check_index(x-1,y) and x-1>=0:
            q.append([x-1,y])
        if check_index(x,y-1) and y-1>=0:
            q.append([x,y-1])   
    cnt+=1
    if cnt ==6:
        break
    # print(q)
    for i in result:
        print(i)
