def solution(alp, cop, problems):
    answer = 0
    problems = sorted(problems, key=lambda x : (x[0],x[1],x[-1]))
    print(problems)
    time = 0 
    for idx, p in enumerate(problems):
        need_alp, need_cop, gain_alp, gain_cop, pay_time = p
        # 문제를 못푸는 경우
        if alp < need_alp or cop < need_cop:
            # 알고리즘이 부족했던 경우
            if alp < need_alp:
                time += need_alp - alp
            # 프로그래밍이 부족했던 경우
            if cop < need_cop:
                time += need_cop - cop
        
        # 마지막문제면 break
        if idx + 1 == len(problems):
            break

        # 현재 문제를 해결가능 -> 다음문제 해결하기 위해 현재 문제를 얼마나 더 풀어야 할지
        next_need_alp, next_neex_cop, next_gain_alp, next_gain_cop, next_pay_time = problems[idx + 1]
        if alp < next_need_alp




            
        


    return answer

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]

ans = solution(alp,cop,problems)
print(ans)
