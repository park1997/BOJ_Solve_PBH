num = input()
left_len = 1
right_len = 1
while 1:
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
