import sys
a,b = map(int,sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for i in range(a)]
coin_list.reverse()
count = 0
for i in coin_list:
    if b<i:
        pass
    else:
        c = b//i
        b = b-(i*c)
        count +=c
        if b==0:
            print(count)
