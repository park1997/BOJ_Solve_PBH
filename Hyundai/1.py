import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
dic_s = {}
for idx,s in enumerate(S):
    if s not in dic_s:
        dic_s[s] = [idx]
    else:
        dic_s[s].append(idx)
result = 0
for r in dic_s["R"]:
    for g in dic_s["G"]:
        for b in dic_s["B"]:
            temp_l = [r,g,b]
            temp_l.sort()
            d1 = temp_l[1] - temp_l[0]
            d2 = temp_l[2] - temp_l[1]
            if d1 == d2:
                continue
            result += 1
print(result)
