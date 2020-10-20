a = int(input())

for i in range(a):
    num,string = input().split()
    for j in string:
        print(j*int(num),end="")
    print()
