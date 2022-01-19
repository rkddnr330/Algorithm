#다른 풀이를 보니까 정규표현식을 썼다. 정규표현식을 활용한 풀이가 많더라.

#Sol
import re
p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    test = input()
    if p.match(test): print('Infected!')
    else: print('Good')

