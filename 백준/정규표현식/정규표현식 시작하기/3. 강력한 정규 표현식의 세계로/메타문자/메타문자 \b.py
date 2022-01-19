# 메타문자 \b
# 공백

import re      #메타문자 r 붙여줘야함. 안에 역슬래시 있으므로 고대로 인지시키려고
p = re.compile(r'\bclass\b')    #' class '를 의미

print(p.search('no class at all'))  #<re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm'))   #None
print(p.search('one subclass is'))  #None