# TV 크기
n1,n2,n3 = map(int,input().split())

n1 = n1 * n1
x = (n2*n2) + (n3*n3)
an = (n1/x)
an = an ** 0.5

z = int(n2 * an)
y = int(n3 * an)

print(z,y)