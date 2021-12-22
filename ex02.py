def iscross(v,i,j):
    return  (v[i][0] < v[j][0] and v[i][1] > v[j][1]) or (v[i][0] > v[j][0] and v[i][1] < v[j][1])

N = int(input())
v = [list(map(int,input().split())) for i in range(N)]
v_dic = {}
for i in range(N):
    cnt = 0
    for j in range(N):
        if i==j:
            continue
        if iscross(v,i,j):
            cnt+=1
    v_dic[i] = cnt
v_dic = sorted(v_dic.items(), key = lambda x : x[1], reverse=True)
print(v_dic)
print(v)
result = 0
for _ in range(N):
    flag = False
    v[v_dic[_][0]] = [-1,-1]
    print(v)
    for i in range(_,N):
        cnt = 0
        for j in range(_,N):
            if i == j : continue
            if iscross(v,i,j):
                flag = True
                cnt += 1
                break
        if flag:
            break
    if cnt == 0:
        result = _+1
        break
print(result)

