#1 10개의 소 위치를 담을 10*10 배열 만듦
#2 소 위치 하나 입력받고, 바로 기본 배열에 위치 정보 append
#3 소 위치 정보 담은 배열 돌리면서 위치 달라지면 cnt+1

#sol
array, cnt = [ [] for _ in range(10) ], 0   #같은 줄에서 array, cnt 선언 가능
n=int(input())

for _ in range(n):
    cow,place = map(int,input().split())    
    array[cow-1].append(place)  #기본 소 위치 배열에 위치 history 추가해줌

for i in range(10):
    if len(array[i]) >= 2:  #위치가 바뀐다는 것 = 두번 이상 움직임
        for j in range(len(array[i])-1):
            if array[i][j] != array[i][j+1]: cnt += 1   
            #위치 history의 값을 비교하면서 서로 다르면 cnt +1
    else: pass

print(cnt)