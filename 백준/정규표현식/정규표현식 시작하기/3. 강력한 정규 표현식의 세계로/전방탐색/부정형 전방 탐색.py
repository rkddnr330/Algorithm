# 부정형 전방 탐색

import re

p = re.compile('.*[.](?!bat$|exe$).*$', re.M)   #끝에 bat, exe 빼고 찾아라
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)    #['autoexec.jpg']