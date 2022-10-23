def check(s1, line2):
    for i in range(len(s1)):
        if s1[i] != line2[i]:
            return False
    return True

def solution(line1, line2):
    answer = 0
    space = 1
    l1, l2 = len(line1), len(line2)
    while 1:
        for d in range(l1):
            s1 = ""
            for i in range(d, l1, space):
                s1 += line1[i]
                if len(s1) == l2:
                    break
            if len(s1) == l2 and check(s1, line2):
                answer += 1
        space += 1
        if space * (l2 - 1) >= l1:
            break
    return answer

line1 = "abcabcabc"
line2 = "abc"
r = solution(line1, line2)
print(r)


