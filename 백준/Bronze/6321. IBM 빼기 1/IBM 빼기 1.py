N = int(input())
word_lst = []
for i in range(1,N+1):
    word = input()
    new = ''
    for j in word:
        ascii = ord(j)
        if(ascii == 90):
            ascii = 64
        new += chr(ascii+1)
    word_lst.append(new)

cnt = 1
for i in word_lst:
    print('String #'+str(cnt))
    print(i)
    print('')
    cnt += 1