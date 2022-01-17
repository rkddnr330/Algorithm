#생각
#1 온점으로 확장자 구별해서 따로 구한다
#2 확장자 내림차순
#3 확장자 개수 count
#시간초과. 제한 시간 : 3초
#다른 사람들 보니까 내장함수로 대부분 풀었다. 시간이 10배나 차이남

#sol1 17초
n=int(input())
extens=[]
word_array=[ str(input()) for _ in range(n) ]
for i in word_array:
    word=i.split('.')
    extens.append(word[-1])
extens.sort()
extens_=list(set(extens))
extens_.sort()
for i in extens_:
    print(i+' '+str(extens.count(i)))
