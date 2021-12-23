num = "02894"
num2 = "567"
result = 1
for i in num:
    if int(i) == 0:
        result+=int(i)
    else:
        result*=int(i)
print(result)