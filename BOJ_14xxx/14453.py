# Hoof, Paper, Scissors(Silver)
import sys
N = int(sys.stdin.readline())
snum = []
H = 0
P = 0
S = 0
for i in range(N):
    a = sys.stdin.readline().strip()
    if a == "H":
        H+=1
    elif a =="P":
        P+=1
    elif a=="S":
        S+=1
    snum.append([H,P,S])
r = -1
for i in range(N):
    temp = [0,0,0]
    for j in range(3):
        temp[j]=snum[-1][j]-snum[i][j]
    if r < max(snum[i])+max(temp):
        r = max(snum[i])+max(temp)
print(r)