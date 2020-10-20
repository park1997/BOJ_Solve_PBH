a= int(input())
b=666
count = 0
while True:
    if '666' in str(b):
        count +=1
        if count == a:
            print(b)
            break
    b+=1
