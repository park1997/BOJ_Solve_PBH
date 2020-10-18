b=[]

for i in range(10):
    a=int(input())
    b.append(a%42)



print(len(set(b)))



#또 다른 방법~~~~~~~~~~~~~~~~~~~~~~~~~
#b=[]
#
#for i in range(10):
#    a=int(input())
#    b.append(a%42)
#
#for j in range(43):
#    if j in b:
#       b.remove(j)
#
#print(10-len(b))
