a=input()
a_list=[a[i] for i in range(len(a))]
a_list_num = []
for i in a_list:
    a_list_num.append(int(i))
a_list_num.sort()
num_1 = ""
for i in a_list_num:
    num_1 += str(i)
print(num_1[::-1])
