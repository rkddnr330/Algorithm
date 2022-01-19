#search : '검색', match와 달리 모든 게 일치하지 않아도, 매치되는 게 있으면 찾아서 match객체를 return해준다.

import re
p = re.compile('[a-z]+')

m1 = p.search('python')
m2 = p.search('3 python')

print(m1)   #<re.Match object; span=(0, 6), match='python'>
print(m2)   #<re.Match object; span=(2, 8), match='python'>
            #match되는 부분인 python을 return해준다.