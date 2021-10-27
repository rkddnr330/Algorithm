#이중배열
n=int(input())
arr = [[1] for _ in range(n)]
for _ in range(9):
    arr[0].append(1)
for k in range(2,n+1):
    for j in range(1,10):
        for i in range(j):
            arr[k]+=int(arr[k-1][i])
print(sum(arr[n]))
