n=int(input())
list = [ input() for _ in range(n)]
for word in list:
    check=[]
    if len(word) == 1: pass
    else:
        cnt=0
        for l in range(len(word)):
            if cnt == 1: break

            if word[l] not in check:
                check.append(word[l])
            elif word[l] in check:
                if check[-1] == word[l]:
                    check.append(word[l])
                else: 
                    n -=1
                    cnt+=1
print(n)
