def dfs(s):
    global r,l,visited, graph,cnt
    cnt += 1
    for i in graph[s]:
        if not visited[i]:
            visited[i] = True
            if cnt%2==0:
                if i not in r:
                    r.append(i)
                    dfs(i)
                else:
                    return False
            else:
                if i not in l:
                    l.append(i)
                    dfs(i)
                else:
                    return False
    return True
V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = False
for i in range(1,V):
    r = []
    l = []
    visited = [False]*(V+1)
    cnt = 0
    if dfs(i):
        print(1)
    else:
        print(2)
        flag = True
if flag:
    print("NO")
else:
    print("YES")


