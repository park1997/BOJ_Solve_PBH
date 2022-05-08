def solution(new_id):
    answer = new_id
    # 1
    new_id = new_id.lower()
    # 2
    temp_id = ""
    for s in new_id:
        if (97<=ord(s)<=122) or (s in ["-","_","."]) or (48<=ord(s)<=57):
            temp_id += s
    new_id = temp_id
    # 3
    while 1:
        if ".." in new_id:
            new_id = new_id.replace("..",".")
        else:
            break
    # 4
    while 1:
        flag =True
        if new_id[0] == ".":
            new_id = new_id[1:]
            flag = False
        if len(new_id) == 0:
            break
        if new_id[-1] == ".":
            new_id = new_id[:-1]
            flag = False
        if len(new_id) == 0:
            break
        if flag:
            break
    # 5
    if len(new_id) == 0:
        new_id = "a"
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while 1:
            if new_id[-1] == ".":
                new_id = new_id[:-1]
            else:
                break
    # 7
    if len(new_id) <= 2:
        while 1:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break
    answer = new_id
    return answer




answer = solution("123_.def")
print(answer)