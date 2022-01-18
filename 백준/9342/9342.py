#이게 왜 맞지? 코드 개더럽다
#효율적으로 하는 방법을 모르겠어서 if문을 파고 들어가서 조건 하나하나 걸러줬다
#마지막에 AFC 하나 예외처리해줬다
#내가 모르는 예외가 하나 더 있을줄 알았는데 없었다. 답은 맞았으나 얻어걸린듯
#교훈 : 코테에서도 잘 몰라도 최대한 구현하다보면 이렇게 맞을 일이 생길 수가 있다!

check, k, ans = 'ABCDEF', 'AFC',''  #참고할 것들 선언
for _ in range(int(input())):
    word=str(input())
    if word[-1] not in check and word[-1] != 'C': ans='x'   #첫글자 또는 마지막 글자부터 예외 찾기
    else:
        if 'A' not in word[0:2]: ans='x'    #첫번째, 두번째엔 무조건 A가 있어야 함. 
        else:
            if word[0] not in check: ans='x'    #A 없더라도 첫글자가 ABCDEF 에 있어야 함
            else:
                if word[1] not in k[0:2]: ans='x'   #두번째 글자는 A나 F 둘중에 하나여야함
                else:
                    a=word[2:]  #이제 A.. F.. C.. 뭉텅이 판별하기
                    a_=[]

                    for i in a: #반복된 거 뺴주는 과정
                        if i not in a_: a_.append(i)
                        else:
                            pass
                    a_=''.join(a_)

                    if len(a_) >= 2 and a_ in k: ans='o'

                    else: #만약 4글자일 경우 (예외)
                        a_=[]
                        for i in word[:-1]:
                            if i not in a_: a_.append(i)
                            else: pass
                        a_=''.join(a_)
                        if a_ == k: ans='o'
                        else: ans='x'
                        
    if word == k: ans='o'   #하나의 예외 : AFC

    if ans == 'o': print('Infected!')
    else: print('Good')