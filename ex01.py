from collections import deque
F,S,G,U,D = map(int,input().split())
ele = [0]*(F+1)
q = deque()
q.append(S)
ele[S] = 1
dx = [U,-D]
flag = False
while q:
    a = q.popleft()
    if a == G:
        flag = True
        break
    for i in range(2):
        nx = a + dx[i]
        if 0<nx<len(ele) and ele[nx]==0 :
            q.append(nx)
            ele[nx] = ele[a] + 1
if flag:
    print(ele[G]-1)
else:
    print("use the stairs")
