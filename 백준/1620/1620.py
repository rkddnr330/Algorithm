#생각
#1 포켓몬 도감 완성
#2 찾기
#3 숫자일 때, 문자일 때 구분해서 print하기
#시간초과

#sol
n,q = map(int,input().split())
pocket=[str(input()) for _ in range(n)]

for _ in range(q):
    test=input()
    if test.isdigit():
        print(pocket[int(test)-1])
    else:
        print(pocket.index(test)+1)
