from decimal import Decimal

def magneticForce(index, x, m):
    start = Decimal(x[index])
    end = Decimal(x[index+1])
    for _ in range(100):
        mid = Decimal(Decimal(start + end) / Decimal(2.0))
        force = Decimal(0.0)

        for i in range(0, index + 1, 1):
            force += Decimal(m[i]) / Decimal((x[i] - mid) * (x[i] - mid))

        for i in range(N - 1, index, -1):
            force -= Decimal(m[i]) / Decimal((x[i] - mid) * (x[i] - mid))
        
        if force > 0:
            start = mid
        else:
            end = mid
    return mid

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    temp_magnetic = list(map(int, input().split()))
    result = []
    x = []
    m = []
    for i in range(N):
        x.append(temp_magnetic[i])
    for j in range(N, 2 * N, 1):
        m.append(temp_magnetic[j])
    
    for index in range(N - 1):
        r = magneticForce(index, x, m)
        result.append(r)
        
    for r in result:
        print("#{} {:.10f}".format(test_case, r), end = " ")
    print()

