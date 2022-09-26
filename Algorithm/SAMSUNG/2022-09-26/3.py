
nums = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
strs = {0 : "ZRO", 1 : "ONE", 2 : "TWO", 3 : "THR", 4 : "FOR", 5 : "FIV", 6 : "SIX", 7 : "SVN", 8 : "EGT", 9 : "NIN"}
T = int(input())
for test_case in range(1, T + 1):
    tc, length = map(str, input().split())
    temp_list = [nums[c] for c in list(map(str, input().split()))]
    temp_list.sort()
    r = [strs[t] for t in temp_list]
    print("#{}".format(test_case))
    print(*r)
