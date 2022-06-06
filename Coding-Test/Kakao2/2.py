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
# 싸이클을 어떻게 찾아야할까?
# 일차원으로 만들어서 투포인터로 



def solution2(queue1,queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1,s2 = sum(q1), sum(q2)

    if s1 == s2:
        return 0
    else:
        ans = -2
        cnt = 0
        upper = 300000
        while cnt < upper:
            if s1 > s2:
                x = q1.popleft()
                s1 -= x
                q2.append(x)
                s2 += x
            elif s1 < s2:
                x = q2.popleft()
                s2 -= x
                q1.append(x)
                s1 += x
            cnt += 1
            if s1 == s2:
                return cnt
    return -1

queue1 = [3,2,7,2]
queue2 = [4,6,5,1]

result = solution2(queue1,queue2)
print(result)

