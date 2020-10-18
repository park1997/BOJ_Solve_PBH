import sys

inp = int(input())

for i in range(inp):
    b,c = map(int,sys.stdin.readline().split())
    print(b+c)
