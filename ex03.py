def my_Func(start, end=0, hop =1):
    if start > end :
        init_val = 0
        while init_val < start+1:
            yield init_val
            init_val += hop
    else:
        init_val = start
        while init_val < end +1:
            yield init_val
            init_val += hop 

for i in my_Func(5):
    print(i)
print()
for i in my_Func(1,5):
    print(i)
print()
for i in my_Func(1,5,2):
    print(i)
