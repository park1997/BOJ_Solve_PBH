import sys

string = sys.stdin.readline().strip().upper()
s = list(string)

dict = {}

for spell in s:
    if spell not in dict.keys():
        dict[spell] = 1
    else:
        dict[spell] += 1

max_value = 0
max_key = ""
print(dict)
flag = True
for key in dict.keys():
    if dict[key] > max_value:
        max_value = dict[key]
        max_key = key
    elif dict[key] == max_value:
        print("?")
        flag = False
        break

if flag:
    print(max_key)