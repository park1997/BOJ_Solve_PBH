s = "abcc"
s_list = []
slice = 0

for i in range(1,len(s)):
    start = 0
    while True:
        print(s[start : start + i])
        start += 1
        if start + i == len(s) - 1:
            break
