# Yangjojang of The Year
for i in range(int(input())):
    dic = {}
    for j in range(int(input())):
        name, quantity = map(str,input().split())
        dic[name] = int(quantity)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic[0][0])