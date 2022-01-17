#단어 중 숫자만 골라내면 됨
#숫자 목록을 str로 만들어 in, not in 사용함

#sol
num, finding ='0123456789',[]   #num 만들어줌

for i in str(input()):
    if i not in num: finding.append(i)  #숫자 제외한 문자 따로 빼주기
finding=''.join(finding)    #list를 str로 합치기

if str(input()) in finding:
    print(1)
else: print(0)
