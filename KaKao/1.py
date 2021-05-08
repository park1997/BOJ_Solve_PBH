def solution(s):
    s = s+" "
    d = {'one' : '1', 'two' : 'w', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for i in d:
        start=0
        end = len(i)
        while 1:
            if s[start:end] == i:
                s = s[0:start]+d[i]+s[end:]
            start+=1
            end+=1
            if end>len(s):
                break
    return int(s.strip())
print(solution("123"))

