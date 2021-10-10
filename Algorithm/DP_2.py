'''
1로 만들기

정수 X가 주어졌을 떼, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지 입니다.
1. X가 5로 나누어 떨어지면 5로 나눕니다.
2. X가 3으로 나누어 떨어지면, 3으로 나눕니다
3. X가 2로 나누어 떨어지면 2로 나눕니다.
4. X에서 1을 뺍니다.
정수 X가 주어졌을 떄, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다.
연산을 사용하는 횟수의 최솟값을 출력하세요. 예를들어 정수가 26이면 다음과 같이 계산해서 3번의
연산이 최솟값 입니다.
26 -> 25 -> 5 -> 1
'''

num = int(input())
dp = [0]*num
if num==1 or num ==2 or num==3 or num==5:
    print(1)
elif num==4:
    print(2)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 1

    for i in range(5,num):
        temp = []
        if (i+1)%2==0:
            temp.append(dp[i//2]+1)
        if (i+1)%3==0:
            temp.append(dp[i//3]+1)
        if (i+1)%5==0:
            temp.append(dp[i//5]+1)
        temp.append(dp[i-1]+1)
        dp[i] = min(temp)
print(dp[-1])


