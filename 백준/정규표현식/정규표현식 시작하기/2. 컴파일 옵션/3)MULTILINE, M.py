# MULTILINE, M
# 꺽쇄(^)를 맨 처음만이 아닌 각 라인의 처음으로 인식시키는 옵션
import re

p1 = re.compile("^python\s\w+")
                #^ : 맨 처음에  ...  ^python = python으로 시작하는~
                #\s : (space) 공백
                #\w : (word) 알파벳, 숫자, _ 중 하나
                #^python\s\w+ : 'python 글자여러개'

data = """python one
life is too short
python two
you need python
python three"""

print(p1.findall(data))    #['python one']  ...  맨 처음에 python one으로 시작

p2 = re.compile('^python\s\w+',re.M)

print(p2.findall(data))    #['python one', 'python two', 'python three']
                           #MULTILINE 옵션 -> 뒤에 줄도 새로운 줄로 인식하게 함. 그래서 첫 시작으로 읽기 때문에 여러 개 return