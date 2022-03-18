# 쌍의 합
for _ in range(int(input())):
    tmp = ""
    a = int(input())
    if a in [1,2]:
        print("Pairs for {}:{}".format(a,tmp))
    else:
        for i in range(1,(a//2)+1):
            if i != a-i:
                tmp+=" {} {},".format(i,a-i)
        print("Pairs for {}:{}".format(a,tmp[:-1]))