a=int(input())
num = a-len(str(a))*9
def sum(x):
    c=0
    for i in str(x):
        c += int(i)
    return x+c
a_list = []
a_sum=0
a_real_sum = 0
if a>=18:
    for j in range(num,a):
        if a == sum(j):
            a_list.append(j)
            break
else:
    for j in range(a):
        if a == sum(j):
            a_list.append(j)
            break
if len(a_list) == 0:
    print(0)
else:
    print(a_list[0])
