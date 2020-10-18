a_list=list(range(10000))
a=[i+1 for i in a_list]
b=[]
for i in range(10000):
    a_1000=0
    a_100=0
    a_10=0
    a_1=0
    if len(str(a[i]))==4:
        a_1000=a[i]%10 + ((a[i]-(a[i]%10))%100)//10 + ((a[i]-(a[i]%100))%1000)//100 + a[i]//1000
    if len(str(a[i]))==3:
        a_100 = a[i]%10+((a[i]-(a[i]%10))//10)%10+(a[i]-(a[i]%100))//100
    if len(str(a[i]))==2:
        a_10=a[i]//10+a[i]%10
    if len(str(a[i]))==1:
        a_1=a[i]
    a_cal=a_1 + a_10 + a_100 + a_1000 + a[i]
    b.append(a_cal)
    b.append(a_cal)
new_list=list(set(a)-set(b))
for k in range(len(new_list)):
    new_list.sort()
    print(new_list[k])
