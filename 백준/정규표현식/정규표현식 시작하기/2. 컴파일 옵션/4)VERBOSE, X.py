# VERBOSE, X
# 복잡한 정규표현식 라인 나눠서 쓸 수 있게 만들어주는 옵션 -> 공백들을 제거해줌
# 원래는 줄 바꿔서 쓰면 안됨

import re
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
                    #이렇게 긴 정규표현식이 있을 때
charref = re.compile(r"""
 &[#]
 (
     0[0-7]+
    |[0-9]+
    |x[0-9a-fA-F]+
 )
 ;
""", re.VERBOSE)    #VERBOSE or X 옵션으로 나눠 쓸 수 있게 만들어주는 옵션