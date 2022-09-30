from itertools import permutations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    company = None
    house = None
    route = []
    for i in range(N + 2):
        if i == 0:
            company = [data[2 * i], data[2 * i + 1]]
        elif i == 1:
            house = [data[2 * i], data[2 * i + 1]]
        else:
            route.append([data[2 * i], data[2 * i + 1]])
    permu = list(permutations(route, N))
    result = int(1e9)
    for p in permu:
        flag = False
        temp_result = abs(company[0] - p[0][0]) + abs(company[1] - p[0][1])
        temp_result += abs(house[0] - p[-1][0]) + abs(house[1] - p[-1][1])
        for d in range(N - 1):
            start = p[d]
            end = p[d + 1]
            temp_result += abs(start[0] - end[0]) + abs(start[1] - end[1])
            if temp_result >= result:
                True
                break
        if flag:
            continue

        result = min(result, temp_result)
    print("#{} {}".format(test_case, result))

