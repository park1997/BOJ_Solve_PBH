import sys
a=int(sys.stdin.readline())
b=[int(sys.stdin.readline()) for i in range(a)]
b_list=[]
for i in b:
    if i!=0:
        b_list.append(i)
    else:
        b_list.pop()
print(sum(b_list))
