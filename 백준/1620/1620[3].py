# 이전 풀이에서 시간초과됐던 이유
# 도감에서 포켓몬 찾을 때 탐색하는 데에 시간이 걸린 거였음
# 딕셔너리의 key, value를 이용한다면 탐색할 필요 없다

#sol
import sys

input=sys.stdin.readline

n,q = map(int,input().split())
dic, dic_number = [], {}

for i in range(n):
    mon=input().rstrip()
    dic.append(mon)
    dic_number[mon]=i+1

for _ in range(q):
    test=input().rstrip()
    if test.isdigit() : print(dic[int(test)-1])
    else: print(dic_number[test])