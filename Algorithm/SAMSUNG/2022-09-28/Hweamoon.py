from collections import deque
def palindrome():
    for num in range(100, 0, -1):
        for i in range(100):
            for j in range(100):
                # 길이가 넘어 가는 경우
                if j + num > 100:
                    break
                # 가로
                temp_string = "".join(graph[i][j : j + num])
                if temp_string == temp_string[::-1]:
                    return len(temp_string)

                if i + num > 100:
                    break
                # 세로
                temp_string2 = ""
                for k in range(num):
                    temp_string2 += graph[i+k][j]
                if temp_string2 == temp_string2[::-1]:
                    return len(temp_string2)


T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    graph = [list(input()) for _ in range(100)]
    r = palindrome()
    print("#{} {}".format(tc, r))



'''
1
C B C A B B A C 
B B A B C A B A
A B C B C A C A
B A C C A A B B
B C B C A C B C
C A B A C C C B
C A A A C C A B
C B A B A C A C
'''