def factorial(x):
    if x==0:
        return 1
    else:
        sum=x*factorial(x-1)
        return sum
print(factorial(3))

def sum_1(x):
    if x==1:
        return 1
    else:
        sum = x +sum_1(x-1)
        return sum
print(sum_1(10))

def fibo(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        sum = fibo(x-1)+fibo(x-2)
        return sum
print(fibo(10))

def hanoi(x,a,b,c):
    if x==1:
        
    else:
        hanoi(x-1,a,c,b)

    pass
print(hanoi(10,a,b,c))
