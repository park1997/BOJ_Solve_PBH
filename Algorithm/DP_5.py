'''
병사 배치하기
N명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다.
다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.
또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 
그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶습니다.

입력예시
7
15 11 4 8 5 2 4
출력예시 
2
'''
N = int(input())
data = list(map(int,input().split()))
dp = [1] * N
for i in range(1,N):
    for j in range(i):
        if data[i]<data[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))

