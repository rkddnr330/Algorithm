# sol2 6초
extens=[ input().split('.')[1] for _ in range(int(input()))]
extens_=list(set(extens))
extens_.sort()
for i in extens_:
    print(i+' '+str(extens.count(i)))
