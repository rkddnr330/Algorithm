#findall  ...  일치하는 str을 list에 담아서 return해준다
#finditer  ...  iterator object를 return해준다

import re
p = re.compile('[a-z]+')

m1 = p.findall('life is too short')     
m2 = p.finditer('life is too short')

print(m1)   #['life', 'is', 'too', 'short']
print(m2)   #<callable_iterator object at 0x7fa3a7a11490>

#finditer를 매치객체로 꺼내기  ...  iterator object -> 매치객체
for i in m2:
    print(i)
    #<re.Match object; span=(0, 4), match='life'>
    #<re.Match object; span=(5, 7), match='is'>
    #<re.Match object; span=(8, 11), match='too'>
    #<re.Match object; span=(12, 17), match='short'>