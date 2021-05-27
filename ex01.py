a= 1
while 1:
    if a*(a+1)/2 >=3000:
        result = a*(a+1)//2
        loc = a
        break
    a+=1
print("1~1000의 합에서 최초로 3000이 넘는 위치 :",loc)
print("숫자의 합은 :",result)