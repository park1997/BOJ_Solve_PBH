#단어공부
sentence = input().upper()
alpha_num_list = [0]*26
for i in sentence:
    alpha_num_list[ord(i)-65]+=1

if alpha_num_list.count(max(alpha_num_list))!=1:
    print("?")

else:
    print(chr(alpha_num_list.index(max(alpha_num_list))+65))
