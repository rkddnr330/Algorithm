# Greedy, Non-Greedy : ?
# ? 이걸 이용하면 탐욕을 제한할 수 있다

import re

s = '<html><head><title>Title</title>'

#Greedy
print(re.match('<.*>', s).group())  #<html><head><title>Title</title>

#Noon-Greedy
print(re.match('<.*?>', s).group()) #<html>