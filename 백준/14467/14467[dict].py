#처음에 dictonary 개념을 이용하여 풀 수 있지 않을가 생각함
#dict 이용하지 못한 이유 : 위치 history정보를 다 입력하여 풀려고 함.
#하지만 dict의 value는 하나밖에 못옴.
#위치 history를 다 담을 필요 없음. 그냥 이전 위치랑 같은지만 비교하고, 위치 바뀌면 바뀐 값 넣고 cnt+1

#sol
cows, cnt = {},0    #cows 딕셔너리, cnt 초기값 설정
for _ in range(int(input())):   #int(input())을 바로 for문의 range에 넣어줌
    cow, position = map(int,input().split())

    if cow not in cows: #cow 정보가 처음이면
        cows[cow] = position   #입력한 position을 value로 설정

    else:   #cow 정보가 처음이 아니면
        if cows[cow] != position:   #value값 비교해서 위치 다르면
            cnt+=1
            cows[cow]=position  #cnt+1 하고 새로운 position 업뎃

print(cnt)