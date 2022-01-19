# 메타문자 |
# or 을 의미

import re

p = re.compile('Crow|Servo')    #Crow 또는 Servo
m = p.match('CrowHello')
print(m)    #<re.Match object; span=(0, 4), match='Crow'>