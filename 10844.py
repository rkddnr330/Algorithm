n=int(input())
arr=[ [0]*10 for _ in range(n+1)]
for i in range(1,10):
    arr[1][i]=1
for j in range(2,n+1):
    for k in range(0,10):
        if k == 0:
            arr[j][k] = arr[j-1][k+1]
        elif k == 9:
            arr[j][k] = arr[j-1][k-1]
        else:
            arr[j][k] = arr[j-1][k-1]+arr[j-1][k+1]
print(sum(arr[n])%1000000000)