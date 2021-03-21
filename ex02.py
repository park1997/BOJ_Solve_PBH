def game(idx, nations_score, probability):
    # 모든 매치가 끝났을 경우
    if idx == 6:
        sorted_score = sorted(list(nations_score.items()), key=lambda x: x[1], reverse=True)
        print(sorted_score)
        # 동점 4명
        if sorted_score[0][1] == sorted_score[1][1] == sorted_score[2][1] == sorted_score[3][1]:
            for i in range(4):
                nations_probability[sorted_score[i][0]] += probability * 1 / 2  # 4팀중 2팀
            return
        # 동점 3명
        elif sorted_score[0][1] > sorted_score[1][1] == sorted_score[2][1] == sorted_score[3][1]:
            nations_probability[sorted_score[0][0]] += probability
            for i in range(1, 4):
                nations_probability[sorted_score[i][0]] += probability * 1 / 3  # 3팀중 1팀
            return
        elif sorted_score[0][1] == sorted_score[1][1] == sorted_score[2][1]:
            for i in range(3):
                nations_probability[sorted_score[i][0]] += probability * 2 / 3  # 3팀중 2팀
            return
        # 동점 2명
        elif sorted_score[0][1] > sorted_score[1][1] == sorted_score[2][1]:
            nations_probability[sorted_score[0][0]] += probability

            for i in range(1, 3):
                nations_probability[sorted_score[i][0]] += probability * 1 / 2  # 2팀중 1팀
            return
        # 동점자 없음
        else:
            for i in range(2):
                nations_probability[sorted_score[i][0]] += probability  # 상위 2팀
            return
    
    # A 승
    nations_score[data[idx][0]] += 3
    game(idx + 1, nations_score, probability * float(data[idx][2]))
    nations_score[data[idx][0]] -= 3

    # 무승부
    nations_score[data[idx][0]] += 1
    nations_score[data[idx][1]] += 1
    game(idx + 1, nations_score, probability * float(data[idx][3]))
    nations_score[data[idx][0]] -= 1
    nations_score[data[idx][1]] -= 1

    # B 승
    nations_score[data[idx][1]] += 3
    game(idx + 1, nations_score, probability * float(data[idx][4]))
    nations_score[data[idx][1]] -= 3
    # print(nations_score)
    # print(nations_probability)

if __name__ == "__main__":

    nations = input().split()
    nations_score = {}
    nations_probability = {}
    data = []

    for key in nations:
        nations_score[key], nations_probability[key] = 0, 0
    # print(nations_score)
    for _ in range(6):
        temp = list(input().split())
        data.append(temp)
    print(data)
    game(0, nations_score, 1)
    # print(nations_score)
    for key in nations:
        print(nations_probability[key])
    # print(nations)
    # print(nations_probability)
    # print(nations_score)