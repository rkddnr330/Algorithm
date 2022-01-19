# 그루핑된 문자열 재참조
# \1

import re

p3 = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m3 = p3.search('park 010-2836-2898')
print(m3.group(1))  #park
         #그룹핑한 첫번째를 가져와라!
                                                           #\1 의 의미    
p4 = re.compile(r'(\b\w+)\s+\1') #(공백 글자여러개)공백 여러개 결과의 첫번째 그룹핑
print(p4.search('Paris in the the rain').group())   #the the
#\1은 미리 결과를 예측해서 정규표현식 안에 가져온다
