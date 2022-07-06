import sys
N = int(sys.stdin.readline())
length = int(sys.stdin.readline())
string = sys.stdin.readline().strip()

target = "I" + "OI" * N
cnt = 0
for s in range(0,len(string)-len(target) + 1 ,1):
    if target == string[s:s+len(target)]:
        cnt += 1
print(cnt)
