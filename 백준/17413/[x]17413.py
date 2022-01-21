# 생각 (문제 풀이 계획부터 잘 안됨)
# 문자열 입력 받아서
# 하나씩 돌면서 <> 구분짓고
# 그게 아니면 반대로 돌려주기 

import sys

sent = list(sys.stdin.readline().rstrip())
start,i =0,0

while i < len(sent) :
    if sent[i] =='<': # < 괄호 열리는 부분 만나면
        while sent[i]!='>': i+=1
        i+=1    # 괄호 닫히면 +1

    elif sent[i].isalnum(): # isalnum() : 숫자나 알파벳을 만나면
        start=i
        while i<len(sent) and sent[i].isalnum():
            i+=1
        tmp = sent[start:i]
        tmp.reverse()
        sent[start:i]=tmp

    else: # 공백을 만나면
        i+=1 # 지나가
print(''.join(sent))
