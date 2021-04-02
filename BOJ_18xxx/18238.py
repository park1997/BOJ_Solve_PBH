# ZOAC 2
a='A'+input()
dic={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
count=0
for i in range(len(a)-1):
    if abs(dic[a[i]]-dic[a[i+1]])<13:
        count+=abs(dic[a[i]]-dic[a[i+1]])
    elif abs(dic[a[i]]-dic[a[i+1]])>13:
        count+=abs(abs(dic[a[i]]-dic[a[i+1]])-26)
    else:
        count+=13
print(count)