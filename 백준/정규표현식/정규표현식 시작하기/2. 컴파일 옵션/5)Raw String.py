# Raw String, 백슬래시 문제
# 정규표현식에서 백슬래시를 활용한 표기가 많다 
# ex) \s : 공백, \w : 알파벳,숫자,_
# 근데 만약 백슬래시를 표기 말고 그대로 활용해서 return하고 싶다면?

#\section
import re

#1.1 \\ = \ , 백슬래시 2개는 1개로 치환된다
p1 = re.compile('\\section')

#1.2 \\\\ = \\, 백슬래시 4개는 2개로 치환
p2 = re.compile('\\\\section')

#2 r (raw str)
p3 = re.compile(r'\section')
                #r을 써주면 뒤의 문자 날 것 그대로 나온다.
