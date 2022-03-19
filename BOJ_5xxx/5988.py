# 홀수일까 짝수일까
for _ in range(int(input())):
    a=input()
    if a[-1] in ['1','3','5','7','9']:
        print("odd")
    else:
        print('even')