import math
import sys
for i in range(int(sys.stdin.readline())):
    b,a=map(int,sys.stdin.readline().split())
    print(math.factorial(a)//(math.factorial(b)*math.factorial(a-b)))
