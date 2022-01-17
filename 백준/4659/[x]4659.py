#조건이 3가지가 있어서 어떻게 묶어 처리할지 감이 안잡혔음
#while문을 통해 하나의 단어에 대해서 판단을 끝내고, 다음 단어로 넘어가는 구조
#기본 값을 True라고 설정하고 세 가지 조건을 거쳐 통과하지 못하면 False를 주는 방식. 
#중간에 끊는 것이 아니고, 세 가지 모든 조건을 통과시키고 나중에 결과값(True,False)를 통해 판단함

#sol
while True:
    vow, vow_cnt,vow_repeat,cons_repeat='aeiou',0,0,0
    check = True
    word=str(input())
    if word == 'end': break

    prev=''   #이전 글자와 비교하기 위해
    for j in word:
        if j in vow:    #모음인 경우
            vow_cnt+=1

            vow_repeat+=1
            cons_repeat=0
            if j == prev:
                if j == 'e' or j == 'o':
                    pass
                else: check=False

            if vow_repeat>=3: check=False

        else:   #자음인 경우
            vow_repeat=0
            cons_repeat+=1

            if j == prev:
                check=False
            if cons_repeat >=3:
                check=False
        prev=j

    if vow_cnt <1 : check=False

    if check:
        print('<'+word+'> is acceptable.')
    else:
        print('<'+word+'> is not acceptable.')
