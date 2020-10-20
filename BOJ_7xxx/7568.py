a=  int(input())
w_list=[]
t_list=[]
for i in range(a):
    w,t = map(int,input().split())
    w_list.append(w)
    t_list.append(t)
count =[1 for i in range(a)]
for j in range(a):
    for k in range(a):
        if w_list[j] < w_list[k] and t_list[j] < t_list[k]:
            count[j] +=1
print(*count)
