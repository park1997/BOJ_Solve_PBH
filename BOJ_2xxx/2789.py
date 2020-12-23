# 유학금지
a=['C','A','M','B','R','I','D','G','E']
b=input()
for i in b:
    if i in a:
        b=b.replace(i,"")
print(b)
