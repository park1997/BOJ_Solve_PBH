a=int(input())

for i in range(2*a-1):
    if i<a-1:
        print("*"*(i+1))
    elif i==a-1:
        print("*"*(i+1))
    else:
        print("*"*(2*a-1-i))
        
