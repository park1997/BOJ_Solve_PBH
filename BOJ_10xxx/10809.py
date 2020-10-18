#알파벳 찾기
a=list(input())

alphabet = []
output = []
for i in range(97,123):
    alphabet.append(chr(i))

for j in range(26):
    output.append(-1)
for k in range(len(a)):
    for i in a:
        num = alphabet.index(i)
        output[num]=a.index(i)

for i in range(len(output)):

    print(output[i], end = " ")

#1등 풀이
#string = input()
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#for i in alphabet:
#    print(string.find(i), end = ' ')
