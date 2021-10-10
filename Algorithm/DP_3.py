'''
N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최고한으로 이용해서 그 가치의 합이 M원아
되도록 하려고 합니다. 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
예를 들어 2원,3월 ㄷㄴ위의 화폐가 있을 때는 15원을 만들기 위해 3월은 5개 사용하는 것이
가장 최소한의 화폐 개수입니다. M원을 만들기 위한 최소한의 화폐개수를 출력하는 프로그램을
작성하세요

입력예시 1
2 15
2
3

입력예시 2
3 4
3
5
7
'''

n,m = map(int,input().split())
coin = [int(input()) for i in range(n)]
dp = [10001]*(m+1)
dp[0] = 0
for i in coin:
    dp[i]=1
# print(dp)
for i in range(n):
    for j in range(coin[i],m+1):
        if dp[j-coin[i]] != 10001:
            dp[j] = min(dp[j],dp[j-coin[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
