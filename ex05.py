from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

due_dates = [5, 12, 32, 16, 23, 25, 26, 27, 30, 15, 7, 22]
proc_times = [4, 6, 7, 7, 5, 4, 7, 6, 8, 4, 3, 6]
intervals = []
start_variables = []
end_variables = []
tardy_variables = []
total_tardiness = []

num_jobs = len(proc_times)

infinity = solver.infinity()
X=[]  #Xij=1 이면 i가 j보다 먼저 스케줄인 경우
C=[]  #completin time
T=[]  #tardiness
for i in range(num_jobs):
    X_temp = []  #X리스트에 2차원 배열로 정열하기 위한 장치
    for j in range(num_jobs):
        X_temp.append(solver.IntVar(0.0, 1.0, 'X_' + str(i+1)+ '_' + str(j+1)))
    X.append(X_temp)
    C.append(solver.NumVar(0, infinity, 'C_' + str(i+1)))
    T.append(solver.NumVar(0, infinity, 'T_' + str(i+1)))

# Add Constraints Here
# i와 j가 다르면 X[i][j] + X[j][i] == 1 이어야만 하기 때문에 다음 조건 추가
for i in range(num_jobs):
    for j in range(num_jobs):
        if i is not j:
            solver.Add(X[i][j] + X[j][i] == 1)

# i의 C.T가 P.T보다 크거나 같다라는 조건 (자명)
for i in range(num_jobs):
    solver.Add(C[i] >= proc_times[i])

# Big M method를 사용하하여 다음과 같은 조건 추가
for i in range(num_jobs):
    for j in range(num_jobs):
        if i is not j:
            solver.Add(C[i]-C[j]+X[i][j]*10000 >= proc_times[i])

# Tardiness의 개념을 고려한 조건 추가
for i in range(num_jobs):
    solver.Add(T[i] >= C[i]-due_dates[i])

solver.Minimize(sum(T))  #Tardiness의 합이 최소가 되도록해라
solver.EnableOutput()     
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())