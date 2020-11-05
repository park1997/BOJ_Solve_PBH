import sys
c = int(sys.stdin.readline())
list_1 = [[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for i in range(c):
    a, b = map(int,sys.stdin.readline().split())
    if a%10 == 0:
        print(10)
    else:
        print(list_1[a%10-1][(b%len(list_1[a%10-1]))-1])
