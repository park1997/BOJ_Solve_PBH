num = str(input())
left_len = 1
right_len = 1
cnt = 0
if len(num) == 1:
    print(num,num)
else:
    while 1:
        # print(num,left_len,right_len)
        if (len(str(left_len))**10 - int(num[:left_len]))*len(str(left_len)) + (len(str(right_len))**10-int(num[-right_len:]))*len(str(right_len)) == len(num):
            break
        # elif (left_len+right_len)%2 == 0:
        #     right_len += 1
        # elif (left_len+right_len)%2 == 1:
        #     left_len += 1
        # print(left_len,right_len)
        else:
            result = ""
            if int(num[:left_len]) < int(num[-right_len:]):
                for i in range(int(num[:left_len]),int(num[-right_len:])+1):
                    result += str(i)
                    if result[:len(result)] != num[:len(result)] :
                        break
                if result == num:
                    break
                else:
                    left_len+=1
            else:
                right_len+=1
            if left_len == len(num) and right_len==len(num):
                break
    print(num[:left_len],num[-right_len:])

print(len(str("456789101112131415161718192021")))
