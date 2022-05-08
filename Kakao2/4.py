
paths =	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# paths_sort = [i[2] for i in paths]
# max_path = max(paths_sort)
# print(paths_sort)
gates = [3,7]
summits = [1,5]
n = 7
def solution(n,paths,gates,summits):
    from ast import iter_child_nodes
    from collections import defaultdict,deque

    dic = defaultdict(list)
    for i,j,c in paths:
        dic[i].append([j,c])
        dic[j].append([i,c])

    real_answer_node ,real_answer_intensity = float('inf'),float('inf')

    for gate in gates:
        print('gate====================',gate)
        # reach_goal = False
        answer_intensity = 0
        answer_node = float('inf')
        d = deque()
        d.append([0,gate])

        visited = [0]*(n+1)
        visited[gate] = 1
        while d:
            intensity,curr_node = d.popleft()
            
    
    
            for next_node,cost in dic[curr_node]:
            
            
                if next_node in gates:
                    if next_node != gate:
                        continue
                if next_node in summits:
                    new_intensity = max(intensity,cost)    
                    if answer_intensity == 0:
                        answer_node = next_node
                        answer_intensity = new_intensity
                        continue
                    if answer_intensity>new_intensity:
                        
                        answer_intensity=new_intensity
                        answer_node = next_node

                    elif answer_intensity==new_intensity:
                        answer_node = min(answer_node,next_node)
            
                else:
                    if not visited[next_node]:
                        visited[next_node]= 1
        
                        d.append([max(intensity,cost) ,next_node])
        
        if real_answer_intensity>answer_intensity:
            real_answer_intensity=answer_intensity
            real_answer_node = answer_node

        elif real_answer_intensity==answer_intensity:
            real_answer_node = min(real_answer_node,answer_node)



    return [real_answer_node,real_answer_intensity]

print(solution(n,paths,gates,summits))