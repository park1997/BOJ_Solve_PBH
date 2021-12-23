print(ord('o'))
s = input()
t1 = 0
t2 = ""
for i in s:
    try:
        t1+=int(i)
    except:
        t2+=i
t2 = sorted(list(t2),key = lambda x: ord(x))
t2 = "".join(t2)
print(str(t2)+str(t1))
