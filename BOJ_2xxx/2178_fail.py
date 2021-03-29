# 미로 찾기
# 미로찾기 알고리즘을 풀었으나 미로가 입구에서 출구까지 갈수있는 미로인지 확인 할수 있음
def check_index(x,y):
    try:
        if miro[y][x]==1:
            return True
        else:
            return False
    except :
        return False
def check_pre(p_x,p_y,x,y):
    if p_x==x and p_y==y:
        return False
    else:
        return True
N,M = map(int,input().split())
miro = []
for i in range(N):
    temp=[]
    for j in input():
        temp.append(int(j))
    miro.append(temp)
pre_x =-1
pre_y =-1
x=0
y=0
cnt=1
temp_x=0
temp_y=0
result=[]
count=0
check = True
while 1:
    count+=1
    # 동
    if check_index(x+1,y) and (x+1<=M-1) and check_pre(pre_x,pre_y,x+1,y):
        pre_x=x
        pre_y=y
        x+=1
        if check:
            cnt+=1
        else:
            cnt-=1
            miro[y][x]=0
    # 남
    elif check_index(x,y+1) and (y+1<=N-1) and check_pre(pre_x,pre_y,x,y+1):
        pre_x=x
        pre_y=y
        y+=1
        if check:
            cnt+=1
        else:
            cnt-=1
            miro[y][x]=0
    # 서
    elif check_index(x-1,y) and (x-1>=0) and check_pre(pre_x,pre_y,x-1,y):
        pre_x=x
        pre_y=y
        x-=1
        if check:
            cnt+=1
        else:
            cnt-=1
            miro[y][x]=0
    # 북
    elif check_index(x,y-1) and (y-1)>=0 and check_pre(pre_x,pre_y,x,y-1):
        pre_x=x
        pre_y=y
        y-=1
        if check:
            cnt+=1
        else:
            cnt-=1
            miro[y][x]=0
    # 막다른길
    else:
        temp_x=x
        temp_y=y
        
        # 이전길로 돌아감
        x=pre_x
        y=pre_y

        pre_x=temp_x
        pre_y=temp_y

        miro[pre_y][pre_x]=0
        cnt-=1
    print(x,y,"   ",pre_x,pre_y,"  ",cnt)
    for i in miro:
        print(i)
    if x==M-1 and y==N-1:
        result.append(cnt)
        check=False
    if count==20:
        break


print(result)
print(min(result))

