def dfs(start,sum,visited):
    visited[start]= True 
    for i in range(N) :
        new_vis = deepcopy(visited)
        new_vis = [v[:] for v in visited]

        if not new_vis[i]:
            sum2 = sum+ abs(nums[start]-nums[i])
            dfs(i,sum2,new_vis)
    
    sums.append(sum)

from copy import deepcopy   

N = int(input())

nums = list(map(int,input().split()))

sums = []


for i in range(N):
    sum = 0 
    visited = [False for i in range(N)] 
    dfs(i,sum,visited)

print(max(sums))

