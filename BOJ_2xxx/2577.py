a=int(input())
b=int(input())
c=int(input())
d=a*b*c
d_list = list(str(d))
for i in range(10):
    count = d_list.count(str(i))
    print(count)
