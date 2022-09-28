T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    s = input()
    target = input()
    print("#{} {}".format(tc, target.count(s)))
    