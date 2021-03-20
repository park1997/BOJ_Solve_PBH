c_list = list(map(str,input().split()))
c_dic={}
c_dic1={}
for i in c_list:
    c_dic[i]=0
    c_dic1[i]=0
for i in range(6):
    result = list(map(str,input().split()))
    if float(result[2]) > float(result[4]) and float(result[2]) > float(result[3]):
        c_dic[result[0]]+=3
    elif float(result[2]) == float(result[4]) and float(result[2]) > float(result[3]):
        c_dic[result[0]]+=1
        c_dic[result[1]]+=1
    elif float(result[2]) < float(result[4]) and float(result[3]) < float(result[4]):
        c_dic[result[1]]+=3
    elif float(result[3])*2 > float(result[2]) + float(result[4]):
        c_dic[result[0]]+=1
        c_dic[result[1]]+=1
c_dic_sorted=sorted(c_dic.items(), key=lambda x:x[1],reverse=True)
c_value_sort = sorted(c_dic.values(),reverse=True)
cnt=0
if c_value_sort.count(max(c_value_sort))==4:
    for i in c_dic1:
        c_dic1[i]=0.5
    c_value_sort[0]=-1
    c_value_sort[1]=-1
    c_value_sort[2]=-1
    c_value_sort[3]=-1
    cnt=2
elif c_value_sort.count(max(c_value_sort))==3:
    max_num = max(c_value_sort)
    for i in c_dic:
        if c_dic[i]==max_num:
            c_dic1[i]=2/3
    c_value_sort[0]=-1
    c_value_sort[1]=-1
    c_value_sort[2]=-1
    cnt=2
elif c_value_sort.count(max(c_value_sort))==2:
    max_num= max(c_value_sort)
    for i in c_dic:
        if c_dic[i]==max_num:
            c_dic1[i]=1/2
    c_value_sort[0]=-1
    c_value_sort[1]=-1
    cnt=2
elif c_value_sort.count(max(c_value_sort))==1:
    max_num= max(c_value_sort)
    for i in c_dic:
        if c_dic[i]==max_num:
            c_dic1[i]=1
            break
    c_value_sort[0]=-1
    cnt=1


if c_value_sort.count(max(c_value_sort))==3 and cnt!=2:
    max_num = max(c_value_sort)
    for i in c_dic:
        if c_dic[i]==max_num:
            c_dic1[i]=1/3
elif c_value_sort.count(max(c_value_sort))==2 and cnt!=2:
    max_num = max(c_value_sort)
    for i in c_dic:
        if c_dic[i] == max_num:
            c_dic1[i]=1/2
elif c_value_sort.count(max(c_value_sort))==1 and cnt!=2:
    max_num = max(c_value_sort)
    for i in c_dic:
        if c_dic[i]==max_num:
            c_dic1[i]=1
            break
for i in c_dic1:
    print("{}".format(float(c_dic1[i])))

# print(c_dic)
