T = int(input())
for i in range(T):
    n = int(input())
    sticker = [list(map(int,input().split())) for j in range(2)]
    if n==1:
        print(max(sticker[0][0],sticker[1][0]))
        continue
    for k in range(1,n):
        if k == 1:
            sticker[0][1] += sticker[1][0]
            sticker[1][1] += sticker[0][0]
        else:
            sticker[0][k] += max(sticker[1][k-1],sticker[1][k-2])
            sticker[1][k] += max(sticker[0][k-1],sticker[0][k-2])
    print(max(sticker[0][-1],sticker[1][-1]))