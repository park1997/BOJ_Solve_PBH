N = int(input())
h = 0
m = 0
s = 0
cnt = 0
while str(h)+str(m)+str(s)!=str(N)+"5959":
    if s<59:
        s+=1
    else:
        s = 0
        if m<59:
            m += 1
        else:
            m=0
            h+=1
    if "3" in str(h)+str(m)+str(s):
        cnt+=1
print(cnt)

