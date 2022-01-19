# DOTALL, S
# Dot(.) 쓸 때 줄바꿈 (\n)도 포함하게 매치시킨다

import re
p1 = re.compile('a.b')
m1 = p1.match('a\nb')
print(m1)   #None, 왜냐하면 .은 줄바꿈을 제외한 문자이기 때문

p2 = re.compile('a.b',re.DOTALL)
m2 = p2.match('a\nb')
print(m2)   #<re.Match object; span=(0, 3), match='a\nb'>
            #줄바꿈 문자가 있어도 객체가 매칭돼서 나옴
            #DOTALL 옵션이 줄바꿈도 포함하게 만들었기 때문

p3 = re.compile('a.b',re.S) #re.DOTALL = re.S
m3 = p3.match('a\nb')   
print(m3)   #<re.Match object; span=(0, 3), match='a\nb'>
            #DOTALL 대신 S 써도 됨
