from itertools import combinations
a,b=map(int,input().split())
card = list(map(int,input().split()))
card_combi =list(combinations(card,3))
card_combi_sum = [sum(i) for i in card_combi]
card_combi_sum.sort()
card_combi_sum.reverse()
for i in range(len(card_combi_sum)):
    if card_combi_sum[i]>b:
        continue
    else:
        print(card_combi_sum[i])
        break
