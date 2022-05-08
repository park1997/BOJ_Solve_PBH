from collections import deque
def solution(queue1,queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1,s2 = sum(queue1),sum(queue2)
    if s1 == s2:
        return 0
    else:
        answer = -2 
        cnt = 0
        upper = 300000
        while cnt < upper:
            if s1 > s2:
                x = q1.popleft()
                s1 -= x
                y = q2.append(x)
                s2 += x
            else:
                x = q2.popleft()
                s2 -= x
                y = q1.append(x)
                s1 += x
            cnt += 1 
            if s1 == s2: 
                answer = cnt
                return answer
    return -1