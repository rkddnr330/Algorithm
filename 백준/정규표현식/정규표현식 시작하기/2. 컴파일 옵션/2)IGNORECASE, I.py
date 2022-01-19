# IGNORECASE, I
# 대,소문자 구분없이 매칭해주는 옵션

import re

p1 = re.compile('[a-z]') #영어 소문자 아무거나 한개

print(p1.match('python'))   #<re.Match object; span=(0, 1), match='p'>
print(p1.match('Python'))   #Non e
print(p1.match('PYTHON'))   #None

p2 = re.compile('[a-z]',re.I)   #re.I = re.IGNORECASE

print(p2.match('python'))   #<re.Match object; span=(0, 1), match='p'>
print(p2.match('Python'))   #<re.Match object; span=(0, 1), match='P'>
print(p2.match('PYTHON'))   #<re.Match object; span=(0, 1), match='P'>
                            #대소문자 상관없이 p,P를 매칭해줌
