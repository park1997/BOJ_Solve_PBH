#최대공약수와 최소공배수
import sys
import math
a,b=map(int,sys.stdin.readline().split())
print(math.gcd(a,b))
print((a*b)//math.gcd(a,b))
