file_in = open("notice.txt",'r',encoding='utf-8')
inStr = file_in.readline()

wordlist = list(map(str,inStr.split()))
str_word = ['파이썬','기말','주의','답안']

count_word = [0]*len(str_word)

for i in range(0,len(str_word)):
    for word in wordlist:
        if str_word[i] in word:
            count_word[i] +=1
print(count_word)
