def main(): 
    t,num,string= map(str,input().split())
    num = int(num)
    result =[]
    for i in range(len(string)):
        cnt = 0
        temp = ""
        for j in string[i:len(string)]:
            temp+=j
            if j==t:
                cnt+=1
            if cnt>num:
                break
            else:
                result.append(temp)
    max_len = len(result[0])
    index = 0
    for i in result:
        if len(i) > max_len:
            max_len = len(i)
            index = string.index(i) + 1
    print(index,max_len)

if __name__=="__main__": 
    main()
