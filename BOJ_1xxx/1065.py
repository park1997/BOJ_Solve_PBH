a = int(input())
a_100 = 0



if a<100:
    print(a)

if a>=100:
    for i in range(100,a+1):
        a_list = list(str(i))
        for j in range(len(a_list)):
            a_list[j]=int(a_list[j])
        if (a_list[1]-a_list[0])==(a_list[2]-a_list[1]):
            a_100 +=1
        else:
            pass

    print(99 + a_100)
