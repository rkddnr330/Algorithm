t=int(input())
ans=[]
for i in range(t):
    n,m = map(int,input().split())
    s = list(map(int,input().split()))
    s_ = [ 0 for _ in range(n)]
    s_[m] = 1   
    #자리를 구별하기 위해 a,b,c 아스키코드로 변환하려 했는데 내가 알고 싶은 위치만 1로 표시를 해주었따
    #다른 위치는 필요가 없는 셈.

    cnt = 0
    while True: #break가 뜰 때까지 무한 반복하겠다는 소리

        #for문을 이용하여 인덱스 값으로 다루려 했는데 
        #어차피 맨 앞의 수를 다루니까 s[0]으로 다뤘다. 더 간편함
        if s[0] == max(s):
            cnt+=1
            if s_[0] == 1:
                ans.append(cnt)
                break
            else:
                del s[0]    #remove보다 del이 더 편리함
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]
for i in ans:
    print(i)
