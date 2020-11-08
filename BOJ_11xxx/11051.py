#이항 계수 2
from math import factorial
import sys
a,b=map(int,sys.stdin.readline().split())
print((factorial(a)//(factorial(b)*factorial(a-b)))%10007)
