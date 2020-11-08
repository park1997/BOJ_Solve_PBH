#이항계수1
from itertools import combinations
a,b=map(int,input().split())
print(len(list(combinations(range(a),b))))
