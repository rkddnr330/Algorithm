# 긍정형 전방 탐색 (?=)
# 검색 조건엔 포함되나, 결과엔 포함 안됨

import re

p = re.compile(".+(?=:)")   #:까지 포함
m = p.search("http://google.com")
print(m.group())    #http