n= int(input())
arr=[ input().split() for _ in range(n)]
ans=[]
for i in range(len(arr)):
    num=1
    for man in arr:
        if int(arr[i][0])<int(man[0]) and int(arr[i][1])<int(man[1]):
            num+=1
    ans.append(num)
for i in ans:
    print(i, end=' ')