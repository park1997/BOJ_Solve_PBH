a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int,input().split())))
    average = (float(sum(b[i]))-float(b[i][0]))/float(b[i][0])
    count_more_than_avg = 0.0
    for j in b[i][1:]:
        if j > average:
            count_more_than_avg+=1


    print("{:.3f}%".format(round(count_more_than_avg/float(b[i][0])*100,3)))
