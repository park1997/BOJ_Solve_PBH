a= int(input())
b_list = []
for i in range(a):
    b = int(input())
    b_list.append(b)
b_list.sort()
for j in range(len(b_list)):
    print(b_list[j])
