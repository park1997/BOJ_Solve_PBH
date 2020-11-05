a_list={0:0,1:1,2:1}
def f(n):
    if n in a_list:
        return a_list[n]
    else:
        a_list[n] = f(n-2) + f(n-1)
        return a_list[n]
print(f(int(input())))
