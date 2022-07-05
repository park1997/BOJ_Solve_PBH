import sys
def switching(sex, switch_num):
    global switch
    if sex == 1:
        count = 1
        while count * switch_num <= N:
            change = count * switch_num
            if switch[change - 1]:
                switch[change - 1] = 0
            elif not switch[change - 1]:
                switch[change - 1] = 1
            count += 1
    elif sex == 2:
        switch_num -= 1
        start = switch_num - 1
        end = switch_num + 1
        cnt = 0
        check = None
        while 1:
            if start <= -1 or end >= N:
                check = [cnt, start + 1, end - 1]
                break
            if switch[start] == switch[end]:
                cnt += 1
                start -= 1
                end += 1
            else:
                check = [cnt,start + 1, end - 1]
                break
        for i in range(check[1],check[2]+1,1):
            if switch[i]:
                switch[i] = 0
            elif not switch[i]:
                switch[i] = 1


N = int(sys.stdin.readline())
switch = list(map(int,sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())
order = []
for _ in range(student_num):
    sex, switch_num = map(int,sys.stdin.readline().split())
    switching(sex,switch_num)
    # print(switch)

cnt = 0
for i in range(len(switch)):
    print(switch[i], end=" ")
    cnt += 1
    if cnt % 20 == 0:
        print()