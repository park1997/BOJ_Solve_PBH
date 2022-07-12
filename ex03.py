import sys
paper = [0]
for _ in range(6):
    paper.append(int(sys.stdin.readline()))

# 6
result = paper[6]
# paper[6] = 0

# 5
for i in range(paper[5]):
    result += 1
    paper[5] -= 1
    for j in range(11):
        if paper[1] > 0:
            paper[1] -= 1

# 4
for i in range(paper[4]):
    cnt4 = 0
    result += 1
    paper[4] -= 1
    for j in range(5):
        if paper[2] > 0:
            paper[2] -= 1
            cnt4 += 1
    if cnt4 == 5:
        continue
    for k in range(20 - cnt4 * 4):
        if paper[1] > 0:
            paper[1] -= 1
    


# 3
if paper[3] >= 4:
    result += paper[3] // 4
    paper[3] = paper[3] % 4
    # while True:
    #     paper[3] -= 4
    #     result += 1
    #     if paper[3] < 4:
    #         break
cnt3 = 0
if paper[3] == 3:
    result += 1
    # paper[3] -= 3
    if paper[2] > 0:
        paper[2] -= 1
        if paper[1] > 0:
            for i in range(5):
                if paper[1] > 0:
                    paper[1] -= 1
    elif paper[2] == 0:
        for j in range(9):
            if paper[1] > 0:
                paper[1] -= 1
elif paper[3] == 2:
    result += 1
    # paper[3] -= 2
    for i in range(3):
        if paper[2] > 0:
            paper[2] -= 1
            cnt3 += 1
    for j in range(18 - cnt3 * 4):
        if paper[1] > 0:
            paper[1] -= 1
elif paper[3] == 1:
    result += 1
    # paper[3] -= 1
    for i in range(5):
        if paper[2] > 0:
            paper[2] -= 1
            cnt3 += 1
    for j in range(27 - cnt3 * 4):
        if paper[1] > 0:
            paper[1] -= 1

# 2
if paper[2] >= 9:
    result += paper[2] // 9
    paper[2] = paper[2] % 9
    
    # while True:
    #     paper[2] -= 9
    #     result += 1
    #     if paper[2] < 9:
    #         break

if paper[2] > 0:
    result += 1
    for i in range(36 - paper[2]* 4):
        if paper[1] > 0:
            paper[1] -= 1
    # paper[2] = 0


# 1
if paper[1] >= 36:
    result += paper[1] // 36
    paper[1] = paper[1] % 36

    # while True:
    #     paper[1] -= 36
    #     result += 1
    #     if paper[1] < 36:
    #         break

if paper[1] > 0:
    result += 1

print(result)






