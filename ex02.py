import sys
from itertools import combinations
from collections import deque
def main():
    def simulation():

        belt[1].append(belt[0].pop())
        belt[0].appendleft(belt[1].popleft())
        for b in belt:
            print(b)
        print()

        robot[0].pop()
        robot[0].appendleft(0)

        if robot[0][2] == 0 and belt[0][2] >= 1:
            robot[0][2] = 1
            robot[0][1] = 0
            belt[0][2] -= 1
        # 로봇올리기
        if belt[0][0] != 0:
            robot[0][0] = 1
            belt[0][0] -= 1
        print("robot")
        for r in robot:
            print(r)
        print()
        print("belt")
        for b in belt:
            print(b)
        print()
        print("-"*10)
        
            


        return 
    N,K = map(int,sys.stdin.readline().split())
    A = list(map(int,sys.stdin.readline().split()))
    a1 = deque()
    for i in range(N):
        a1.append(A[i])
    a2 = deque()
    for j in range(2*N-1,N-1,-1):
        a2.append(A[j])
    belt = [a1,a2]
    robot = []
    for _ in range(2):
        temp = deque()
        for i in range(N):
            temp.append(0)
        robot.append(temp)
    print("robot")
    for r in robot:
        print(r)
    print()
    print("belt")
    for b in belt:
        print(b)
    print()
    print("-"*10)
    
    if belt[0][0] != 0:
        robot[0][0] = 1
        belt[0][0] -= 1
    cnt = 0
    while 1:
        cnt += 1
        simulation()
        result = 0
        for i in belt[0]:
            if i == 0 :
                result += 1
        for j in belt[1]:
            if j == 0:
                result += 1
        if result >= K:
            break

    print(cnt)
    return 



if __name__ == '__main__':
    main()