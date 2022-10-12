# 카드게임
import sys
card = []
for i in range(5):
    temp = []
    a,b = map(str,sys.stdin.readline().strip().split())
    temp.append(a)
    temp.append(int(b))
    card.append(temp)
card = list(sorted(card,key = lambda x: x[1]))
# 1
if card[0][0] == card[1][0] == card[2][0] == card[3][0] == card[4][0] and (card[0][1]+1 == card[1][1] and card[1][1] + 1 == card[2][1] and card[2][1]+1 == card[3][1] and card[3][1]+1 == card[4][1]):
    print(card[4][1]+900)
# 2
elif ((card[0][1] == card[1][1] == card[2][1] == card[3][1]) and card[0][1]!=card[4][1]) or ((card[0][1] == card[1][1] == card[2][1] == card[4][1]) and card[0][1]!=card[3][1]) or ((card[0][1] == card[1][1] == card[4][1] == card[3][1]) and card[0][1]!=card[2][1]) or ((card[0][1] == card[4][1] == card[2][1] == card[3][1]) and card[0][1]!=card[1][1]) or ((card[4][1] == card[1][1] == card[2][1] == card[3][1]) and card[0][1]!=card[4][1]):
    if ((card[0][1] == card[1][1] == card[2][1] == card[3][1]) and card[0][1]!=card[4][1]):
        print(card[0][1]+800)
    elif ((card[0][1] == card[1][1] == card[2][1] == card[4][1]) and card[0][1]!=card[3][1]):
        print(card[0][1]+800)
    elif ((card[0][1] == card[1][1] == card[4][1] == card[3][1]) and card[0][1]!=card[2][1]):
        print(card[0][1]+800)
    elif ((card[0][1] == card[4][1] == card[2][1] == card[3][1]) and card[0][1]!=card[1][1]):
        print(card[0][1]+800)
    elif ((card[4][1] == card[1][1] == card[2][1] == card[3][1]) and card[0][1]!=card[4][1]):
        print(card[4][1]+800)
# 3
elif ((card[0][1]==card[1][1]==card[2][1]) and (card[3][1]==card[4][1])) or ((card[0][1]==card[1][1]==card[3][1]) and (card[2][1]==card[4][1])) or ((card[0][1]==card[1][1]==card[4][1]) and (card[2][1]==card[3][1])) or ((card[1][1]==card[2][1]==card[3][1]) and (card[0][1]==card[4][1])) or ((card[1][1]==card[2][1]==card[4][1]) and (card[0][1]==card[3][1])) or ((card[2][1]==card[3][1]==card[4][1]) and (card[0][1]==card[1][1])):
    if (card[0][1]==card[1][1]==card[2][1]) and (card[3][1]==card[4][1]):
        print(card[0][1]*10 + card[3][1] + 700)
    elif (card[0][1]==card[1][1]==card[3][1]) and (card[2][1]==card[4][1]):
        print(card[0][1]*10 + card[2][1] + 700)
    elif (card[0][1]==card[1][1]==card[4][1]) and (card[2][1]==card[3][1]):
        print(card[0][1]*10 + card[2][1] + 700)
    elif (card[1][1]==card[2][1]==card[3][1]) and (card[0][1]==card[4][1]):
        print(card[1][1]*10 + card[0][1] + 700)
    elif (card[1][1]==card[2][1]==card[4][1]) and (card[0][1]==card[3][1]):
        print(card[1][1]*10 + card[0][1] + 700)
    elif (card[2][1]==card[3][1]==card[4][1]) and (card[0][1]==card[1][1]):
        print(card[2][1]*10 + card[0][1] + 700)
# 4
elif card[0][0] == card[1][0] == card[2][0] == card[3][0] == card[4][0]:
    print(card[4][1] + 600)
# 5
elif (card[0][1]+1 == card[1][1] and card[1][1] + 1 == card[2][1] and card[2][1]+1 == card[3][1] and card[3][1]+1 == card[4][1]):
    print(card[4][1] + 500)
# 6
elif (card[0][1]==card[1][1]==card[2][1]) or (card[0][1]==card[1][1]==card[3][1]) or (card[0][1]==card[1][1]==card[4][1]) or (card[1][1]==card[2][1]==card[3][1])or (card[1][1]==card[2][1]==card[4][1])or (card[2][1]==card[3][1]==card[4][1]):
    if (card[0][1]==card[1][1]==card[2][1]):
        print(card[0][1]+400)
    elif (card[0][1]==card[1][1]==card[3][1]):
        print(card[0][1]+400)
    elif (card[0][1]==card[1][1]==card[4][1]):
        print(card[0][1]+400)
    elif (card[1][1]==card[2][1]==card[3][1]):
        print(card[1][1]+400)
    elif (card[1][1]==card[2][1]==card[4][1]):
        print(card[1][1]+400)
    elif (card[2][1]==card[3][1]==card[4][1]):
        print(card[2][1]+400)
# 7
elif (card[0][1]==card[1][1] and (card[2][1]==card[3][1] or card[2][1]==card[4][1] or card[3][1]==card[4][1])) or (card[0][1]==card[2][1] and (card[1][1]==card[3][1] or card[1][1]==card[4][1] or card[3][1]==card[4][1])) or (card[0][1]==card[3][1] and (card[1][1]==card[2][1] or card[1][1]==card[4][1] or card[2][1]==card[4][1])) or (card[0][1]==card[4][1] and (card[1][1]==card[2][1] or card[1][1]==card[3][1] or card[2][1]==card[3][1])) or (card[1][1]==card[2][1] and (card[0][1]==card[3][1] or card[0][1]==card[4][1] or card[3][1]==card[4][1])) or (card[1][1]==card[3][1] and (card[0][1]==card[2][1] or card[0][1]==card[4][1] or card[2][1]==card[4][1])) or (card[1][1]==card[4][1] and (card[0][1]==card[2][1] or card[0][1]==card[3][1] or card[2][1]==card[3][1])) or (card[2][1]==card[3][1] and (card[0][1]==card[1][1] or card[0][1]==card[4][1] or card[1][1]==card[4][1])) or (card[2][1]==card[4][1] and (card[0][1]==card[1][1] or card[0][1]==card[3][1] or card[1][1]==card[3][1])) or (card[3][1]==card[4][1] and (card[0][1]==card[1][1] or card[0][1]==card[2][1] or card[1][1]==card[2][1])):
    if (card[0][1]==card[1][1] and (card[2][1]==card[3][1] or card[2][1]==card[4][1] or card[3][1]==card[4][1])):
        a = 0
        if card[2][1]==card[3][1]:
            a = card[2][1]
        elif card[2][1]==card[4][1]:
            a = card[2][1]
        elif card[3][1]==card[4][1]:
            a = card[3][1]
        
        if card[0][1]<a:
            print(a*10 + card[0][1] + 300)
        else:
            print(card[0][1]*10 + a + 300)
    elif (card[0][1]==card[2][1] and (card[1][1]==card[3][1] or card[1][1]==card[4][1] or card[3][1]==card[4][1])):
        a = 0
        if card[1][1]==card[3][1]:
            a = card[1][1]
        elif card[1][1]==card[4][1]:
            a = card[1][1]
        elif card[3][1]==card[4][1]:
            a = card[3][1]
        
        if card[0][1]<a:
            print(a*10 + card[0][1] + 300)
        else:
            print(card[0][1]*10 + a + 300)
    elif (card[0][1]==card[3][1] and (card[1][1]==card[2][1] or card[1][1]==card[4][1] or card[2][1]==card[4][1])):
        a = 0
        if card[1][1]==card[2][1]:
            a = card[1][1]
        elif card[1][1]==card[4][1]:
            a = card[1][1]
        elif card[2][1]==card[4][1]:
            a = card[2][1]
        if card[0][1]<a:
            print(a*10 + card[0][1] + 300)
        else:
            print(card[0][1]*10 + a + 300)
    elif (card[0][1]==card[4][1] and (card[1][1]==card[2][1] or card[1][1]==card[3][1] or card[2][1]==card[3][1])):
        a = 0
        if card[1][1]==card[2][1]:
            a = card[1][1]
        elif card[1][1]==card[3][1]:
            a = card[1][1]
        elif card[2][1]==card[3][1]:
            a = card[2][1]
        
        if card[0][1]<a:
            print(a*10 + card[0][1] + 300)
        else:
            print(card[0][1]*10 + a + 300)
    elif (card[1][1]==card[2][1] and (card[0][1]==card[3][1] or card[0][1]==card[4][1] or card[3][1]==card[4][1])):
        a = 0
        if card[0][1]==card[3][1]:
            a = card[0][1]
        elif card[0][1]==card[4][1]:
            a = card[0][1]
        elif card[3][1]==card[4][1]:
            a = card[3][1]
        if card[1][1]<a:
            print(a*10 + card[1][1] + 300)
        else:
            print(card[1][1]*10 + a + 300)
    elif (card[1][1]==card[3][1] and (card[0][1]==card[2][1] or card[0][1]==card[4][1] or card[2][1]==card[4][1])):
        a = 0
        if card[0][1]==card[2][1]:
            a = card[0][1]
        elif card[0][1]==card[4][1]:
            a = card[0][1]
        elif card[2][1]==card[4][1]:
            a = card[2][1]

        if card[1][1]<a:
            print(a*10 + card[1][1] + 300)
        else:
            print(card[1][1]*10 + a + 300)
    elif (card[1][1]==card[4][1] and (card[0][1]==card[2][1] or card[0][1]==card[3][1] or card[2][1]==card[3][1])):
        a = 0
        if card[0][1]==card[2][1]:
            a = card[0][1]
        elif card[0][1]==card[3][1]:
            a = card[0][1]
        elif card[2][1]==card[3][1]:
            a = card[2][1]
        if card[1][1]<a:
            print(a*10 + card[1][1] + 300)
        else:
            print(card[1][1]*10 + a + 300)
    elif (card[2][1]==card[3][1] and (card[0][1]==card[1][1] or card[0][1]==card[4][1] or card[1][1]==card[4][1])):
        a = 0
        if card[0][1]==card[1][1]:
            a = card[0][1]
        elif card[0][1]==card[4][1]:
            a = card[0][1]
        elif card[1][1]==card[4][1]:
            a = card[1][1]
        if card[2][1]<a:
            print(a*10 + card[2][1] + 300)
        else:
            print(card[2][1]*10 + a + 300)
    elif (card[2][1]==card[4][1] and (card[0][1]==card[1][1] or card[0][1]==card[3][1] or card[1][1]==card[3][1])):
        a = 0
        if card[0][1]==card[1][1]:
            a = card[0][1]
        elif card[0][1]==card[3][1]:
            a = card[0][1]
        elif card[1][1]==card[3][1]:
            a = card[1][1]
        if card[2][1]<a:
            print(a*10 + card[2][1] + 300)
        else:
            print(card[2][1]*10 + a + 300)
    elif (card[3][1]==card[4][1] and (card[0][1]==card[1][1] or card[0][1]==card[2][1] or card[1][1]==card[2][1])):
        a = 0
        if card[0][1]==card[1][1]:
            a = card[0][1]
        elif card[0][1]==card[2][1]:
            a = card[0][1]
        elif card[1][1]==card[2][1]:
            a = card[1][1]
        if card[3][1]<a:
            print(a*10 + card[3][1] + 300)
        else:
            print(card[3][1]*10 + a + 300)
# 8
elif (card[0][1]==card[1][1]) or (card[0][1]==card[2][1]) or (card[0][1]==card[3][1]) or (card[0][1]==card[4][1]) or (card[1][1]==card[2][1]) or (card[1][1]==card[3][1]) or (card[1][1]==card[4][1]) or (card[2][1]==card[3][1]) or (card[2][1]==card[4][1]) or (card[3][1]==card[4][1]):
    if card[0][1]==card[1][1]:
        print(card[0][1] + 200)
    elif card[0][1]==card[2][1]:
        print(card[0][1] + 200)
    elif card[0][1]==card[3][1]:
        print(card[0][1] + 200)
    elif card[0][1]==card[4][1]:
        print(card[0][1] + 200)
    elif card[1][1]==card[2][1]:
        print(card[1][1] + 200)
    elif card[1][1]==card[3][1]:
        print(card[1][1] + 200)
    elif card[1][1]==card[4][1]:
        print(card[1][1] + 200)
    elif card[2][1]==card[3][1]:
        print(card[2][1] + 200)
    elif card[2][1]==card[4][1]:
        print(card[2][1] + 200)
    elif card[3][1]==card[4][1]:
        print(card[3][1] + 200)
# 9
else:
    print(card[4][1] + 100)

