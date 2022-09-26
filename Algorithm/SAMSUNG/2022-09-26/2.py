dic = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}

T = int(input())
for test_case in range(1, T + 1):
    odd = 0
    even = 0
    result = []
    N, M = map(int, input().split())
    flag = False
    f1 = True
    f2 = True
    f3 = True
    for s in range(N):
        string = input()
        if "1" not in string or flag:
            continue
        else:
            flag = True

        index1 = string.index("1")
        if string[index1 - 3 : index1 + 4] in dic and f1:
            print("asd",string[index1 - 3 : index1 + 4])
            real = string[index1 - 3 : index1 + 53]
            print("ddddd",real)
            for i in range(0, 56, 7):
                try:
                    result.append(dic[real[i : i + 7]])
                except:
                    f1 = False
                    flag = False
                    result = []
                    continue
        elif string[index1 - 2 : index1 + 5] in dic and f2:
            print("asd",string[index1 - 2 : index1 + 5])
            real = string[index1 - 2 : index1 + 54]
            for i in range(0, 56, 7):
                try:
                    result.append(dic[real[i : i + 7]])
                except:
                    f2 = False
                    flag = False
                    result = []
                    continue
        elif string[index1 - 1 : index1 + 6] in dic and f3:
            real = string[index1 - 1 : index1 + 55]
            for i in range(0, 56, 7):
                try:
                    result.append(dic[real[i : i + 7]])
                except:
                    f3 = False
                    flag = False
                    result = []
                    continue
        
        
        for idx, j in enumerate(result):
            if idx % 2 == 0:
                even += j
            else:
                odd += j
        
        if (even * 3 + odd) % 10 == 0:
            print("#{} {}".format(test_case,even + odd))
        else:
            print("#{} 0".format(test_case))
            
        