# 네 번째수
d_list = list(map(int,input().split()))
d_list.sort()
if d_list[0] + 2*(d_list[1] - d_list[0]) == d_list[2]:
    print(d_list[0]+3*(d_list[1]-d_list[0]))
elif d_list[0] + 3*(d_list[1] - d_list[0]) == d_list[2]:
    print(d_list[0]+2*(d_list[1] - d_list[0]))
elif d_list[0] + int(3/2*(d_list[1] - d_list[0])) == d_list[2]:
    print(d_list[0]+int(1/2*(d_list[1] - d_list[0])))