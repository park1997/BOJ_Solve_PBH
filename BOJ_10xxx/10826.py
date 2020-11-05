n= int(input())
a_list=[0,1,1]
for i in range(3,n+1):
    a_list.append(a_list[i-1]+a_list[i-2])
print(a_list[n])
