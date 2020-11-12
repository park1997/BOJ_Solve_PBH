n = int(input())
for i in range(n):
    print(' ' * (n-i-1), end='')
    print('*'*(i*2+1))
for i in range(1,n):
    print(' ' * i, end='')
    print('*'*((n*2)-(i*2+1)))
