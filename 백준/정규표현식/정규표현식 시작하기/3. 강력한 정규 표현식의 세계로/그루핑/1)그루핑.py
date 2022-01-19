# 그룹핑 ()
# 정규표현식에서 어떤 것을 타겟팅할지 그룹화시킴
import re

p1 = re.compile('ABC+')
m1 = p1.search('ABCABCABC OK?')

print(m1)    #<re.Match object; span=(0, 3), match='ABC'>
print(m1.group())    #ABC

p2 = re.compile('(ABC)+')   #그룹핑
m2 = p2.search('ABCABCABC OK?')

print(m2)    #<re.Match object; span=(0, 9), match='ABCABCABC'>
print(m2.group())    #ABCABCABC

