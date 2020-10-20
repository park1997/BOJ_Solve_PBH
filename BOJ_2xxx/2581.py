a = int(input())
b = int(input())
numbers = [i for i in range(a,b+1)]
real_numbers = [i for i in range(a,b+1)]
if 1 in real_numbers:
    real_numbers.remove(1)

for j in numbers:
    for k in range(2,j):
        if j%k == 0:
            real_numbers.remove(j)
            break


if len(real_numbers)== 0 :
    print(-1)
else:
    print(sum(real_numbers))
    print(real_numbers[0])
