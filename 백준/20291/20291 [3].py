#sol3 1.7초
ans={}
for _ in range(int(input())):
    extens = input().split('.')[1]
    if extens not in ans:
        ans[extens]=1
    else:
        ans[extens]+=1
#딕셔너리들의 키 값만 따로 리스트로 만들 수 있다
ans_=list(ans.keys())
ans_.sort()
for i in ans_:
    print(i, ans[i])

