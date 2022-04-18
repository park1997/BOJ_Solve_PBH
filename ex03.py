import sys
from collections import deque
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
s = deque()
index = 0
result = []
result_num = []
for i in range(1,n+1):
    s.append(i)
    result.append("+")
    if i == li[index]:
        while s:
            if s[-1] == li[index]:
                result.append("-")
                result_num.append(s.pop())
                index += 1
            else:
                break
if result_num == li:
    for r in result:
        print(r)
else:
    print("NO")
