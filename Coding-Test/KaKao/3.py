def solution(n, k, cmd):
    state = k 
    prev_state = []
    example = ["a{}".format(i) for i in range(n)]
    head = -1
    for i in cmd:
        if i[0]=="D":
            state += int(i.split()[1])
        if i[0]=="C":
            prev_state.append([state,example[state]])
            head+=1
            del example[state]
            if state == len(example):
                state-=1
        if i[0]=='U':
            state -= int(i.split()[1])
        if i[0]=='Z':
            example.insert(prev_state[head][0],prev_state[head][1])
            if int(prev_state[head][0])<state:
                state+=1
            head-=1
    print(head)
    result=["X"]*n
    cnt=0
    for i in example:
        result[int(i[1:])]='O'
    result1 = "".join(result)
    return result1
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))