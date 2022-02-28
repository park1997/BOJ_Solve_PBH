# 접미사 배열
s = input()
tmp=[s[i:] for i in range(len(s))]
tmp.sort()
for i in tmp:
    print(i)

