import sys
from collections import Counter
a=int(sys.stdin.readline())
b_list=[int(sys.stdin.readline()) for i in range(a)]
c=[0]*4
if a==1:
    print(b_list[0])
    print(b_list[0])
    print(b_list[0])
    print(0)
else:
    b_list.sort()
    c[0] = round(sum(b_list)/len(b_list))
    c[1] = b_list[len(b_list)//2]
    c[3] = abs(b_list[-1]-b_list[0])
    if len(set(b_list))>2 and Counter(b_list).most_common()[0][1] == Counter(b_list).most_common()[1][1]:
        c[2]=Counter(b_list).most_common()[1][0]
    else:
        c[2] = Counter(b_list).most_common()[0][0]
    for i in c:
        print(i)
