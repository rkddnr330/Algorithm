word = str(input())
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro:
    word = word.replace(i,'a')
print(len(word))

# 내가 생각한 풀이
# str에 인덱싱으로 끊어서 cro에 겹치는 게 있으면 cnt+1해준다.
# 근데 이 방법은 너무 불편하고 코드가 길다. str을 인덱싱으로 만지는 게 좀 복잡하다 나한테

#이 방법
#str의 replace를 활용했음
#replace가 str에서 해당하는 거를 찾아서 원하는 걸로 바꿔주는 것
#수를 출력하는 방법은 크로아티아 문자를 그냥 알파벳 a로 replace하고 
#전체 길이 len을 출력해준다.
