#match객체 다루기
import re

p = re.compile('[a-z]+')
m = p.match('python')

print(m)    #<re.Match object; span=(0, 6), match='python'>
print(m.group())    #python
print(m.start())    #0
print(m.end())      #6
print(m.span())     #(0,6)
