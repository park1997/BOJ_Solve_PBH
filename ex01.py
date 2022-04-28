from itertools import combinations
ans = 0
nums = [1, 2, 3, 4]
sosu = [0] * (max(nums)*3)
for j in range(2,int((max(nums)*3)**(1/2)),1):
    mul = 2
    while mul*j<len(sosu):
        sosu[mul*j] = 1
        mul += 1
    
numbers = list(combinations(nums,3))
print(numbers)
for i in numbers:
    if sosu[sum(i)] == 0:
        ans += 1
print(ans)