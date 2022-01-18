#수학 규칙이 있는 걸까?
#배열을 자유자재로 다루는 느낌이 든다
#n*n 배열을 만들고 숫자가 줄어드는 방향으로 넣어줘야할까? : 다루기 너무 어렵

N = int(input())    #N*N
w = int(input())    #좌표를 구하고 싶은 수
li = [[0 for i in range(N)] for j in range(N)]  #N*N배열
n = 1
    
x = y = N // 2  #x,y : 2로 나눈 몫
check = 2 
li[x][y] = n    #n은 1, 중간점 (시작점)을 1로 설정
i = 0
j = 0
while li[0][0] != N**2: #맨왼쪽위 값이 N**2가 되면 종료 = 다 채웠단 뜻
    x -= 1  #up
    for i in range(check):  #초기 check=2인 이유 : 처음 1,2 채울때 두개를 채우기 때문
        n += 1  #넣을 값 1씩 추가
        li[x][y+i] = n  #y+i : 오른쪽으로 한칸씩
        if n == w:  #for문 돌면서 동시에 좌표 구하고 싶은 수도 찾는다. 찾으면 ans에 바로 저장
            ans = [x+1, y+i+1]
    y += i  #right
    for i in range(1, check+1):
        n += 1
        li[x+i][y] = n
        if n == w:
            ans = [x+i+1, y+1]
    x += i  #down
    for i in range(1, check+1):
        n += 1
        li[x][y-i] = n
        if n == w:
            ans = [x+1, y-i+1]
    y -= i  #left
    for i in range(1, check+1):
        n += 1
        li[x-i][y] = n
        if n == w:
            ans = [x-i+1, y+1]
    x -= i
    check += 2

for i in range(N):
    for j in range(N):
        print(li[i][j], end = ' ')
    print()
print(*ans)