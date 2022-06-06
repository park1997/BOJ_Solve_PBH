from collections import defaultdict
def solution(survey,choices):
    ans_dic = defaultdict(int)
    for i,j in zip(survey,choices):
        left_st,right_st = list(i)
        if j - 4 < 0:
            plus = 4 - j
            ans_dic[left_st] += plus
        elif j - 4 > 0:
            plus = j - 4
            ans_dic[right_st] += plus
    answer = ""
    arr =[["R T"],["C F"],["J M"],["A N"]]
    for i in arr:
        x,y = i[0].split()
        if ans_dic[x] < ans_dic[y]:
            answer += y
        elif ans_dic[x] > ans_dic[y]:
            answer += x
        else:
            if ord(x) > ord(y):
                answer += y
            else:
                answer += x
    return answer


def solution2(survey,choices):
    ans_dic = defaultdict(int)
    plus = 0
    for i,j in zip(survey,choices):
        left,right = list(i)
        if j > 4:
            plus = 4 - j
            ans_dic[left] += plus
        elif j < 4:
            plus = j - 4
            ans_dic[right] += plus
    answer = ""
    arr =[["R T"],["C F"],["J M"],["A N"]]
    for i in arr:
        x,y = i[0].split()
        if ans_dic[x] < ans_dic[y]:
            answer += y
        elif ans_dic[x] > ans_dic[y]:
            answer += x
        else:
            if ord(x) > ord(y):
                answer += y
            else:
                answer += x







survey = ["AN","CF","MJ","RT","NA"]
choices = [5,3,2,7,5]
result = solution2(survey,choices)
print(result)