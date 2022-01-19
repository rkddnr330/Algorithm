# 메타문자 ^
# 맨 처음
import re

      #패턴객체 이용안하고 한 줄에 쓰기
print(re.search('^Life', 'Life is too short'))  #<re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))    #None