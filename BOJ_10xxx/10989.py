import sys
a=int(sys.stdin.readline())
b_list = [0]*10001
for i in range(a):
    b_list[int(sys.stdin.readline())] +=1
for i in range(len(b_list)):
    if b_list[i]!=0:
        for k in range(b_list[i]):
            print(i)
