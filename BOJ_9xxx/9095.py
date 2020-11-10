#1,2,3 더하기
import itertools
Testcase=int(input())
for i in range(Testcase):
    b=int(input())
    list1=[]
    for j in range(b+1):
        a=list(itertools.product(range(1,4), repeat = j+1))
        for k in a:
            if sum(k)==b:
                list1.append(k)
    print(len(list1))
