n=int(input())
z=n
a=0

if n==1:
    print("1/1")

while True:
    a=a+1
    n=n-a
    if n<=0:
        break

result=0
for i in range(a):
    result+=i


if a%2 != 0 :
    print("{}/{}".format(a-(z-result)+1,1+z-result-1))

if a%2 == 0 :
    print("{}/{}".format((1+z-result-1),a-(z-result)+1))
