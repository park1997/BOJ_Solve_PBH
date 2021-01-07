from itertools import combinations
import sys
import math
cycle=int(input("몇번 돌린건지 숫자를 입력하세요 재화니형 ㅎㅎ>>"))
data=list(map(float,input("들어갈 데이터를 띄어쓰기 기준으로 구분하여 입력하세요 재화니형 ㅎㅎ>>").split()))
cnt=0
while 1:
    combi_data=list(combinations(data,2))
    while 1:
        temp=[]
        for i in combi_data:
            temp.append(i[0]+i[1])
            temp.append(i[0]-i[1])
            temp.append(i[0]*i[1])
            try:
                temp.append(round(i[0]/i[1],4))
            except:
                pass
        for i in data:
            try:
                temp.append(round(math.exp(i),4))
            except:
                pass
            try:
                temp.append(round(math.log(i),4))
            except:
                pass
            if i>0:
                temp.append(-i)
            else:
                temp.append(i)
            try:
                temp.append(round(i**-1,4))
            except:
                pass
            temp.append(round(i**2,4))
            temp.append(round(i**3,4))
        data.extend(list(set(temp)))
        cnt+=1
        break
    if cnt==cycle:
        break
print("데이터의 크기:",len(data))
with open('datas.txt', 'w') as f:
    for i in data:
        f.write(str(i)+"\n")
