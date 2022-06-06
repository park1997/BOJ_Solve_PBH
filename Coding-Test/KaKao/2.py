examples = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
sign = True
result =[]
for example in examples:
    for i in range(5):
        for j in range(5):
            if example[i][j]=='P':
                if i+1<5:
                    if example[i+1][j]=='P':
                        sign = False
                        break
                if j+1<5:
                    if example[i][j+1]=='P':
                        sign = False
                        break
                if i+1<5 and j+1<5:
                    if example[i+1][j+1]=='P':
                        if example[i+1][j]=='O':
                            sign = False
                            break
                        if example[i][j+1]=='O':
                            sign = False
                            break
                if i+2<5:
                    if example[i+1][j]=='O' and example[i+2][j]=='P':
                        sign = False
                        break
                if j+2<5:
                    if example[i][j+1]=='O' and example[i][j+2]=='P' :
                        sign = False
                        break
        if not sign:
            break
    if sign:
        result.append(1)
    else:
        result.append(0)
    sign = True
print(result)
    

