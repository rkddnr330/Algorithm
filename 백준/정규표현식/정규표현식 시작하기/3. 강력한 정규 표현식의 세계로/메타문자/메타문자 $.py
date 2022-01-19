# 메타문자 $
# 맨 끝

import re

print(re.search('short$','Life is too short'))  #<re.Match object; span=(12, 17), match='short'>
print(re.search('short$','Life is too short, you need python')) #None