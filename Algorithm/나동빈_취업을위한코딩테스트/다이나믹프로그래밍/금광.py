'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 
'''
for i in range(int(input())):
    n,m = map(int,input().split())
    gold = list(map(int,input().split()))
    t_gold = []
    for j in range(n):
        temp = []
        for k in range(m):
            temp.append(gold[m*j+k])
        t_gold.append(temp)
    max_num = 0
    for i in range(1,m):
        if i==n-1:
            max_num = t_gold[j][i]
        for j in range(n):
            if j==0:
                t_gold[j][i] = max(t_gold[j][i-1],t_gold[j+1][i-1])+t_gold[j][i]
            elif j==n-1:
                t_gold[j][i] = max(t_gold[j][i-1],t_gold[j-1][i-1])+t_gold[j][i]
            else:
                t_gold[j][i] = max(t_gold[j][i-1],t_gold[j+1][i-1],t_gold[j-1][i-1])+t_gold[j][i]
            if t_gold[j][i] > max_num:
                max_num = t_gold[j][i]
    print(max_num)
