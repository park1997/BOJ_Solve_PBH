# 숫자 카드 2
import sys
n = int(sys.stdin.readline())
s1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s2 = list(map(int, sys.stdin.readline().split()))
dic = {}
for n in s1:
    try:
        dic[n] += 1
    except:
        dic[n] = 1
result = []
for i in s2:
    try:
        result.append(dic[i])
    except:
        result.append(0)
for i in result:
    print(i, end = ' ')