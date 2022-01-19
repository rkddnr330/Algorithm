#match 객체
match, search, findall, finditer 하면서 계속 match 객체 얘기를 했다.
도대체 match 객체가 뭐냐?

match 객체의 메서드 1
- .group() : 매치된 문자열을 리턴
- .start() : 매치된 문자열의 시작 위치(index)를 리턴
- .end ()  : 매치된 문자열의 끝 위치(index)를 리턴 #튜플 끝 번호
- .span()  : 매치된 문자열의 (시작,끝)에 해당되는 튜플 리턴