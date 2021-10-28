word=input().split()
word_=[]
for i in word:
    i_=bytearray(i)
    for j in range(len(i)):
        bfr=i_[j]
        n=ord(bfr)
        if (155/2)-n < 0:
            bfr=chr(n+(2*(155/2)-n))
            
        else:
            bfr=chr(n-(2*(155/2)-n))

        i_[j]=bfr
    w=str(i_)
    word_.append(w)
for i in word_:
    print(i, end=' ')