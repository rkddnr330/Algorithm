# 그루핑 이름 붙이기
# ?P<name>

import re
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))  #park

# 그룹 이름을 사용하면 정규표현식에서 재참조하는 것도 가능
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()
'the the'