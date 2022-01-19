#파이썬에서 정규표현식을 지원하는 re모듈
import re   #re 쓰려면 import 해야한다
p = re.compile('ab*')  #정규표현식 넣는 위치
#p : 패턴객체 p가 생긴다

#패턴객체를 이용하는 4가지 방법 : match, search, findall, finditer

#1 match
