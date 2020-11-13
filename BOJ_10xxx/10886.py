#0 = not cute / 1 = cute
a=int(input())
b=[int(input()) for i in range(a)]
if b.count(0)<b.count(1):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
