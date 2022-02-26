# 수학은 체육과목 입니다 3
from sys import stdin
input = stdin.readline

s = input().strip()

def solv():
    if len(s) < 4:
        target = s[0]
        flag = True
        for n in s[1:]:
            if target != n:
                flag = False
                break
        if flag:
            print(s,s)
            return
    for start in range(1,1000):
        tmp_str = str(start)
        if tmp_str[0] == s[0]:
            tmp_str = ''
            for end in range(start,1000):
                tmp_str += str(end)
                if len(tmp_str) == len(s):
                    if tmp_str == s:
                        print(start, end)
                        return
                    else:
                        break
solv()