#match

import re
p = re.compile('[a-z]+')    #정규표현식 의미 : 영어 소문자로 이루어진 모든 글자와 매치됨
#p : 패턴객체

m1 = p.match('python')   #p와 python이 match되는지를 알아보려고
#m1 : 매치객체 생성

m2 = p.match('3 python')    #p와 3 python이 match되는지 알아보려고

print(m1)    # <re.Match object; span=(0, 6), match='python'>
print(m2)    # None  ...  match되지 않으므로 None