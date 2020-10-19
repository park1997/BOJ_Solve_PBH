a=int(input())

for i in range(a):
    b=input()
    output=0
    cnt=0
    for j in range(len(b)):
        if b[j]=="O":
            cnt+=1
            output+=cnt
        elif b[j]=="X":
            cnt=0

    print(output)
