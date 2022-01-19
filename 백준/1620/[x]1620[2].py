# sys를 통해 input에서 걸리는 시간 줄이려 함
# 근데 이것도 시간 초과

#sol
import sys

input = sys.stdin.readline

n,q = map(int,input().split())
pocket=[(input().rstrip()) for _ in range(n)]

for _ in range(q):
    test=input().rstrip()
    if test.isdigit():
        print(pocket[int(test)-1])
    else:
        print(pocket.index(test)+1)

