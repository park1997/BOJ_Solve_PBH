# 투포인터로 풀기
M,K,S = map(str,input().split())
start = 0
end = 0
def count_things(str,m):
    cnt = 0
    for i in str:
        if i==m:
            cnt+=1
    return cnt
result = ""
while end < len(S):
    target = S[start:end]
    if count_things(target,M) > int(K):
        if end == start:
            end+=1
            start+=1
        else:
            start+=1
    else:
        if len(target) > len(result):
            result = target
        end+=1
print(S.index(result)+1,len(result))

# T 0 ATGCAAATTGBT
# T 2 ATGCAAATTGBT
