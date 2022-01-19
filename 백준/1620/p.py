import re

#match
p = re.compile('[a-z]+')
m = p.match('python')
print(m) #match됨. 만약 match 안되면 none이라고 뜸

#search
m = p.search('3 python')
print(m) #python 을 찾아준다

#findall, finditer
m = p.findall('life is too short')
print(m) #['life','is','too','short']

m = p.finditer('life is too short')
for i in m: print(i) #match 객체 형태로 보여줌

#match 객체
print(m.group())
print(m.start())
print(m.end())
print(m.span())